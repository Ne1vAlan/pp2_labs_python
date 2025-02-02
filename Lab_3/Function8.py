def has_007(MyList):
    sequence = [0, 0, 7]
    index = 0

    for i in MyList:
        if i == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False

MyList = list(map(int, input().split()))
Result = has_007(MyList)
print(Result)
