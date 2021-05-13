#9번 C111152 임종욱
import copy
def main():
    global contacts
    contacts = {}
    Input_mod(contacts)
    Print(contacts)
    Del_mod(contacts)
    Index_mod(contacts)
#      저장모드 함수
def Input_mod(contacts):
    while True:
        name = input('이름? ')
        if name == '':# 입력이 엔터면 종료
            return 0
        elif name in contacts: #있는 이름이면 번호리스트에 번호  저장
            while True:
                phone = input('전화번호? ')
                if phone != '':
                    contacts[name] += [phone]
                    break
        else : #없는 이름이면 해당 키에 해당하는 값으로 번호 리스트만들고 번호 저장
            contacts[name] = []
            while True:
                phone = input('전화번호? ')
                if phone != '':
                    break
            contacts[name] += [phone]
#             중복되지 않는 사람,번호 수를 출력
def Print(contacts):
    print('중복되지 않는 사람 수 :',len(contacts))
    global p_num
    p_num = []
    for k in contacts.values():
        p_num += k
    print('중복되지 않는 전화번호 수 :',len(set(p_num)))
    
def Del_mod(contacts):
    global Num_p # 중복되지 않은 번호 
    Num_p = set(p_num)
    while True:
        del_obj = input('지우고 싶은 사람의 이름 또는 전화번호를 입력하세요? ')
        if del_obj == '':# 엔터면 종료
            print('검색모드로 넘어갑니다')
            return 0
        elif del_obj in contacts:  #있는 이름이면 완전 제거
            contacts.pop(del_obj,'')
            print('중복되지 않는 사람의 수 :',len(contacts))
            for i in contacts:
                print(i,end = ' ')
            print()
        elif del_obj in set(p_num): #있는 번호이면 해당 번호 모두 삭제
            contacts_temp = copy.deepcopy(contacts)# 반복문 돌릴때 사용할 임시 연락처
            for j,i in contacts_temp.items():
                if del_obj in i: #번호가 있으면 삭제 
                    i.remove(del_obj)
                    if i == []:# 번호 삭제후 저장된 번호가 없는 사람은 삭제
                        del contacts[j]
                    else: #번호 삭제후 저장된 번호가 있으면 업데이트
                        contacts.update({j:i})
            Num_p.discard(del_obj)     # 남아있는 번호 집합
            print('중복되지 않는 전화번호의 수 :',len(Num_p))
            for i in Num_p:
                print(i,end = ' ')
            print()
# 검색모드
def Index_mod(contacts):
    while 1:
        name_phone = input('찾고싶은 사람의 이름 또는 전화번호를 입력하세요? ')
        if name_phone == '':#입력 엔터면 종료
            print('프로그램을 종료합니다.')
            return 0
        elif name_phone in contacts:# 있는 이름이면 번호 출력
            for i in contacts[name_phone]:
                print(i, end = ' ')
            print()
        elif name_phone in Num_p: #있는 번호이면 이름 출력
            for  k,v in contacts.items():
                if name_phone in v:
                    print(k,end = ' ')
            print()
        else :# 없는 정보이면 출력 
            print(name_phone+'는 등록되지 않았습니다')

    
main()
