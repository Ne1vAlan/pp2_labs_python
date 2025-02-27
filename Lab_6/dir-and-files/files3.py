import os

path =r"D:\gitHub\pp2_labs_python\Lab_6/dir-and-files/file2.py"

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')