#7번문제. C111061 박서연

contacts = {'name' : 'phnum'}

while True:
    name_phnum =(input("이름 또는 전화번호?"))
    
    if name_phnum == '':
        print("프로그램을 종료합니다.")
        break
    
    else:
        if name_phnum in contacts:
            print(name_phnum, "의 전화번호는", contacts.get(name_phnum))
        
        elif name_phnum in contacts.values():
            re_contacts = {v:k for k,v in contacts.items()}
            print("전화번호", name_phnum, "의 소유주는", re_contacts.get(name_phnum))
            
        else:
            if name_phnum.isdigit():
                print("없는 전화번호입니다.")
            else:
                name = name_phnum
                phnum = (input("전화번호?"))
                while phnum == '':
                    phnum = (input("전화번호?"))
                contacts[name] = phnum    