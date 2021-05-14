#6번문제. C111061 박서연 

contacts = dict()

while True:
    name = str(input("이름? "))
    
    if name == "":
        print("프로그램을 종료합니다")
        break
    
    else:
        if name in contacts:
            print(name, "의 전화번호는", contacts.get(name))
        else:
            phnum = str(input("전화번호? "))
            while phnum == "":
                phnum = str(input("전화번호? "))
    
    contacts[name] = phnum
