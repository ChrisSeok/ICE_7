#7번 C111152 임종욱

def main():
    contacts = {}
    while 1:
        name_phone = input('이름 또는 전화번호? ')
        if name_phone == '':# 엔터면 종료
            print('프로그램을 종료합니다.')
            return 0
        elif name_phone in contacts:# 있는 이름이면 번호 출력
            print(name_phone+'의 전화번호는',contacts[name])
        elif name_phone in contacts.values(): # 있는 번호이면 이름 출력
            for  k,v in contacts.items():
                if v == name_phone:
                    print('전화번호',name_phone,'의 소유주는 ',k)
        else :# 없는 이름이면 번호 저장 
            contacts[name_phone] = input('전화번호? ')

main()