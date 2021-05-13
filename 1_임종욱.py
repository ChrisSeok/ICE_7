#1번 C111152 임종욱

def main():
    YYYYMMDD = input('생년월일을 입력하시오: ')
    check(YYYYMMDD)
    
def check(i):
    #생년월일 분리 
    YYYY = int(i[0:4])
    MM = int(i[4:6])
    DD = int(i[6:])
#     leap 윤달 판별
    if YYYY % 400 == 0:
        leap = True
    elif YYYY % 100 == 0:
        leap = False
    elif YYYY % 4 == 0:
        leap = True
    else :
        leap = True
#     윤년의 경우, 변수 c는 올바른 생년월일경우 1아닐경우0
    if leap: 
        if MM in (1,3,5,7,8,10,12):
            if 1 <= DD <= 31:
                c = 1
            else :
                c = 0
        elif MM in (4,6,9,11):
            if 1 <= DD <= 30:
                c = 1
            else :
                c = 0
        elif MM == 2:
            if 1 <= DD <= 29:
                c = 1
            else :
                c = 0
        else :
            c = 0
#  윤년이 아닐 경우 
    else :
        if MM in (1,3,5,7,8,10,12):
            if 1 <= DD <= 31:
                c = 1
            else :
                c = 0
        elif MM in (4,6,9,11):
            if 1 <= DD <= 30:
                c = 1
            else :
                c = 0
        elif MM == 2:
            if 1 <= DD <= 28:
                c = 1
            else :
                c = 0   
        else :
            c = 0
    if c == 0:
        print('잘못된 생년월일입니다.')
    else :
        print('올바른 생년월일입니다.')
    
    
main()