def solve(numheads, numlegs):
    ResultForChicken = (2 * numheads - numlegs // 2)
    ResultForRabbits = numheads - ResultForChicken
    return  ResultForChicken, ResultForRabbits

numheads = 35
numlegs = 94

Chikens, Rabbits = solve(numheads, numlegs)

print("There are:", Chikens, "chikens and", Rabbits, "rabbits on the farm!")