lst = [1, 'is', 'mine', [1, 1, 1], (1, 7), {1: 5}, {1, 4, 5}]

with open('D:/gitHub/pp2_labs_python/Lab_6/dir-and-files/file5.py', 'w') as f:

    f.write(' '.join(map(str, lst)) + '\n')
    
    f.writelines([str(item) + '\n' for item in lst])
