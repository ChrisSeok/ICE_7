# 2번 C111152 임종욱

def main():
    st = input('문자열을 입력하시오: ')
    ch = input('문자를 입력하시오 : ')
    FQ(st,ch)
    #빈도 검사하는 함수
def FQ(st,ch):
    count = 0
    for i in st:
        if i == ch:
            count += 1
    print('\"',ch,'\" 문자의 빈도는',count,'이다')

main()