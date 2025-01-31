def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = float(input("How many grams do you need?:"))
Ounce = grams_to_ounces(grams)
print("Youre ounces:", Ounce)