def rec(x):
    if x == []:
        print("Конец списка")
    else:
        print(x.pop(0))
        rec(x)
        
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

rec(x)