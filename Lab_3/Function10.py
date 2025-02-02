def New_List(List):
    Result = []

    for i in List:
        if i not in Result:
            Result.append(i)
    return Result

List = list(map(int, input().split()))
Result = New_List(List)
print("Your unique list:", Result)