import psycopg2
import csv

# Параметры подключения
params = {
    "dbname": "PhoneBook",
    "user": "postgres",
    "password": "Amfundi10",
    "host": "localhost",
    "port": "5432"
}

# Подключение к базе
print("Connecting to the database...")
conn = psycopg2.connect(**params)
cur = conn.cursor()

# Создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
""")

# Функция поиска
cur.execute("""
    CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
    RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
    BEGIN
        RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        WHERE c.name ILIKE '%' || pattern || '%'
           OR c.phone ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
""")

# Процедура вставки или обновления
cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_or_update_contact(p_name VARCHAR, p_phone VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phone) THEN
            UPDATE contacts SET name = p_name WHERE phone = p_phone;
        ELSE
            INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
        END IF;
    END;
    $$;
""")

# Функция массовой вставки с валидацией
cur.execute(r"""
    CREATE OR REPLACE FUNCTION insert_valid_contacts(
        names TEXT[],
        phones TEXT[]
    )
    RETURNS TABLE(invalid_name TEXT, invalid_phone TEXT) AS $$
    DECLARE
        i INT;
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            IF names[i] IS NULL OR names[i] = ''
               OR phones[i] IS NULL OR phones[i] = ''
               OR phones[i] !~ '^\+7[0-9]{10}$' THEN
                RETURN QUERY SELECT names[i], phones[i];
            ELSE
                INSERT INTO contacts(name, phone) VALUES (names[i], phones[i]);
            END IF;
        END LOOP;
    END;
    $$ LANGUAGE plpgsql;
""")

# Функция пагинации
cur.execute("""
    CREATE OR REPLACE FUNCTION get_contacts_paginated(
        page_limit INT,
        page_offset INT
    )
    RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
    BEGIN
        RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        ORDER BY c.id
        LIMIT page_limit OFFSET page_offset;
    END;
    $$ LANGUAGE plpgsql;
""")

# Процедура удаления по значению
cur.execute("""
    CREATE OR REPLACE PROCEDURE delete_contact_by_value(value TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM contacts
        WHERE name = value OR phone = value;
    END;
    $$;
""")

conn.commit()

# Функции Python
def add_contact():
    name = input("Enter a name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Contact added")

def view_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    print("\n📒 All contacts:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    print()

def search_pattern():
    pattern = input("Enter pattern to search (name or phone): ")
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()
    print("\n🔍 Search results:")
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("No matches found.")
    print()

def update_contact():
    contact_id = input("Enter the contact's ID to update: ")
    new_name = input("New Name: ")
    new_phone = input("New Phone Number: ")
    cur.execute("UPDATE contacts SET name = %s, phone = %s WHERE id = %s", (new_name, new_phone, contact_id))
    conn.commit()
    print("🔄 The contact has been updated!")

def delete_contact():
    contact_id = input("Enter the contact ID to delete: ")
    cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()
    print("🗑️ Contact deleted!")

def delete_by_value():
    value = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_contact_by_value(%s);", (value,))
    conn.commit()
    print(f"🗑️ All contacts with name or phone = '{value}' deleted.")

def load_from_csv():
    file_name = input("Enter the name of the CSV file (e.g., contacts.csv): ")
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
        conn.commit()
        print("📥 CSV data successfully uploaded!")
    except Exception as e:
        print("⚠️ CSV upload error:", e)

def insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL insert_or_update_contact(%s, %s);", (name, phone))
    conn.commit()
    print("ℹ️ Insert or update complete.")

def insert_many_contacts():
    names = input("Enter names (comma-separated): ").split(",")
    phones = input("Enter phones (comma-separated): ").split(",")

    if len(names) != len(phones):
        print("❗ Name and phone count mismatch.")
        return

    cur.execute("SELECT * FROM insert_valid_contacts(%s, %s);", (names, phones))
    invalids = cur.fetchall()

    if invalids:
        print("\n⚠️ Invalid contacts not inserted:")
        for name, phone in invalids:
            print(f"❌ Name: {name}, Phone: {phone}")
    else:
        print("✅ All contacts inserted successfully.")
    conn.commit()

def view_paginated_contacts():
    try:
        limit = int(input("Enter number of contacts per page: "))
        offset = int(input("Enter offset (0 for first page): "))
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
        rows = cur.fetchall()
        print(f"\n📄 Showing {limit} contacts from offset {offset}:")
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("⚠️ No contacts found.")
    except ValueError:
        print("❗ Please enter valid numbers.")

# Меню
while True:
    print("\n===== Menu PhoneBook =====")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Search contact by pattern")
    print("4. Update a contact")
    print("5. Delete contact by ID")
    print("6. Upload contacts from CSV")
    print("7. Insert or update contact (SQL)")
    print("8. Insert many contacts (with validation)")
    print("9. View contacts with pagination")
    print("10. Delete by name or phone (SQL)")
    print("0. Exit")

    choice = input("Select an action: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_pattern()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        load_from_csv()
    elif choice == "7":
        insert_or_update()
    elif choice == "8":
        insert_many_contacts()
    elif choice == "9":
        view_paginated_contacts()
    elif choice == "10":
        delete_by_value()
    elif choice == "0":
        break
    else:
        print("❗ Invalid choice. Try again.")

cur.close()
conn.close()
print("👋 BYE!")
