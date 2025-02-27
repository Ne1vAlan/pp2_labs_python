with open(r"D:\gitHub\pp2_labs_python\Lab_6\dir-and-files\file4.py", 'r') as f1:
    with open(r"D:\gitHub\pp2_labs_python\Lab_6\dir-and-files\file7.py", 'w') as f2:
        f2.write(f1.read())