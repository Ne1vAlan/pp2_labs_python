import os

path = r'D:/gitHub/pp2_labs_python/Lab_6/dir-and-files/file5.A-Z files'

if not os.path.exists(path):
    os.makedirs(path)

A = ord('A')

for i in range(A, A + 26):
    filename = os.path.join(path, f'{chr(i)}.txt')  

    with open(filename, 'w') as f:
        f.write(f"File {chr(i)}")  

print("26 files created successfully.")
