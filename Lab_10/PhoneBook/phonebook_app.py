import psycopg2
import csv

# 🔧 Параметры подключения
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
conn.commit()


# 📞 Добавить контакт вручную
def add_contact():
    name = input("Enter a name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Contact added")


# 📋 Показать все контакты
def view_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    print("\n📒 All contacts:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone number: {row[2]}")
    print()


# 🛠 Обновить контакт
def update_contact():
    contact_id = input("Enter the contact's ID to update: ")
    new_name = input("New Name: ")
    new_phone = input("New Phone Number: ")
    cur.execute("UPDATE contacts SET name = %s, phone = %s WHERE id = %s", (new_name, new_phone, contact_id))
    conn.commit()
    print("🔄 The contact has been updated!")


# 🗑 Удалить контакт
def delete_contact():
    contact_id = input("Enter the contact ID to delete: ")
    cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()
    print("🗑️ Contact deleted!")


# 📁 Загрузка из CSV
def load_from_csv():
    file_name = input("Enter the name of the CSV file (for example, contacts.csv): ")
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                phone = row['phone']
                cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("📥 The CSV data has been successfully added!")
    except Exception as e:
        print("⚠️ Error when uploading the CSV file:", e)


# 🔁 Меню
while True:
    print("\n===== Menu PhoneBook =====")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Upload contacts from a CSV file")
    print("0. Exit")

    choice = input("Select an action: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        load_from_csv()
    elif choice == "0":
        break
    else:
        print("❗ Wrong choice. Try again.")

# Закрытие соединения
cur.close()
conn.close()
print("👋 BYE!")
