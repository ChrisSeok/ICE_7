#8번 C111152 임종욱

def main():
    global contacts
    contacts = {}
    Input()
    Print(contacts)
    Index()
    #연락처 입력모드
def Input():
    while True:
        name = input('이름? ')
        if name == '':# 엔터면 종료
            return 0
        elif name in contacts: #있는 이름이면 번호리스트에 저장
            while True:
                phone = input('전화번호? ')
                if phone != '':
                    contacts[name] += [phone]
                    break
        else :#없는 이름이면 번호리스트 만들고 번호 저장 
            contacts[name] = []
            while True:
                phone = input('전화번호? ')
                if phone != '':
                    break
            contacts[name] += [phone]
#              중복되지 않은 이름 ,번호 수 출력
def Print(contacts):
    print('중복되지 않는 사람 수 :',len(contacts))
    global p_num
    p_num = [] # 번호 리스트
    for k in contacts.values(): # 
        p_num += k
    print('중복되지 않는 전화번호 수 :',len(set(p_num)))#set으로 중복된 번호 삭제후 개수 출력
# 검색모드
def Index():
    while 1:
        name_phone = input('찾고싶은 사람의 이름 또는 전화번호를 입력하세요? ')
        if name_phone == '':# 엔터면 프로그램 종료
            print('프로그램을 종료합니다.')
            return 0
        elif name_phone in contacts: #있는 이름이면 번호 출력
            for i in contacts[name_phone]:
                print(i, end = ' ')
            print()
        elif name_phone in set(p_num):# 있는 번호이면 이름 출력
            for  k,v in contacts.items():
                if name_phone in v:
                    print(k,end = ' ')
            print()
        else :# 없는 번호,이름이면 출력
            print(name_phone+'는 등록되지 않았습니다')

    
main()