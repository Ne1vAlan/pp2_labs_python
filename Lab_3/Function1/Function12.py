def Gistodram(List):
    for i in List:
        print("*" * i)

List = list(map(int, input().split()))
Gistodram(List)
