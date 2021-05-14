#10번문제. C111061 박서연

def mydeepcopy(n):
    copy_n = []
    for item in n:
        if type(item) == type(list()):
            copy_n.append(mydeepcopy(item))
        else:
            copy_n.append(item)
    
    return copy_n
    
def main():
    s = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]]
    d = mydeepcopy(s)
    d[1][1][1][1] = 'xxxxx'
    
    print(d)
    print(s)

main()