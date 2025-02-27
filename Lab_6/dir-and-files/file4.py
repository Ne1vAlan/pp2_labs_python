import os
path = r"D:\gitHub\pp2_labs_python\Lab_6/dir-and-files/file4.py"

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))