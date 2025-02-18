from datetime import datetime

def date_difference_in_seconds(date1, date2):
    format = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(date1, format)
    d2 = datetime.strptime(date2, format)
    difference = abs((d2 - d1).total_seconds())
    return difference


date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

print("Difference in seconds:", date_difference_in_seconds(date1, date2))
