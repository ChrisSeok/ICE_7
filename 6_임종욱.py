# 6번 c111152 임종욱

def main():
    contacts = {}
    while 1:
        name = input('이름? ')
        if name == '': # 입력 엔터면 종료
            return 0
        elif name in contacts: # 있는 이름이면 전화번호 출력
            print(name+'의 전화번호는',contacts[name])
        else : #없는 이름이면 전화번호 저장
            contacts[name] = input('전화번호? ')

main()
