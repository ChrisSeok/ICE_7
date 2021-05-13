#10번, B835193 석채원
def mydeepcopy(obj):
    if(type(obj)is list):
        newlist = list()
        newlist.append(obj[0])
        while(obj):
            mydeepcopy(obj)
      
        return newlist
def main():
 s = ["aaa", ["bbb", ["ccc", ["ddd", "eee", 45]]]]
 d = mydeepcopy(s)
 d[1][1][1][1] = 'xxxxx'
 print(d)
 print(s)
main()