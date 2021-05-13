#10번 C111152 임종욱

def main():
    s = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]]
    d = mydeepcopy(s)
    
    d[1][1][1][1] = 'xxxxx'
    
    print(d)
    print(s)

def mydeepcopy(s):
    copyList = []
    for i in s:
        if type(i) is list:
            copyList += [mydeepcopy(i)]
        else:
            copyList += [i]
    return copyList

main()