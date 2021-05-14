#10번_B735042_김대겸

def main():
    s = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]]
    d = mydeepcopy(s)

    d[1][1][1][1] = 'xxxxx'

    print(d)
    print(s)

def mydeepcopy(x):
    temp = x.copy()
    copy = []
    
    for i in range(len(temp)):
        if (type(temp[i]) in (str, int, float)):
            copy.append(temp[i])
        elif (type(temp[i]) is list):
            copy.append(temp[i])
            mydeepcopy(temp[i])
    return copy

main()
