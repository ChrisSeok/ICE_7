#6번, B835193 석채원
phonebook = dict()
def main():
    while 1:
        name = input("이름?")
        if(name == ''):
            print("프로그램을 종료합니다")
            return
        #이미 입력된 이름일 경우
        elif(name in phonebook):
            print(name,"의 전화번호는",phonebook.get(name))
        #입력되지 않은 이름일 경우 전화번호까지 받아 딕셔너리에 저장
        else:
            while 1:
                phnum = input("전화번호?")
                if(phnum):
                    break
            phonebook[name] = phnum
main()