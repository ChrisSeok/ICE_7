#1번문제. C111061 박서연

birthday = str(input("생년월일을 입력하시오: "))

year = int(birthday[0:4])
month = int(birthday[4:6])
day = int(birthday[6:8])

if 0 < year < 2022:
    check = 'a'

if 0 < month < 13:
    check = 'a'
    
if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if 0 < day < 32:
        check = 'a'
    else:
        check = 'b'
        
        
if month == 4 or 6 or 9 or 11:
    if 0 < day < 31:
        check = 'a'
    else:
        check = 'b'
        
        
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if 0 < day < 30:
            check = 'a'
        else:
            check = 'b'
    else:
        if 0 < day < 29:
            check = 'a'
        else:
            check = 'b'
            
if check == 'a':
    print("올바른 생년월일입니다")
if check == 'b':
    print("올바르지 않은 생년월일입니다")
