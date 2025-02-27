import os 

path = r"D:\gitHub\pp2_labs_python\Lab_6\dir-and-files\file8.py"
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.X_OK):
        print(f'File "{name}" can be eliminated')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be eliminated')
else:
    print(f'File "{name}" does\'t exist')