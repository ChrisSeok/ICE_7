#1번, B835193 석채원
def Wrong():  #틀린 형식일 경우 이 함수를 호출 YYYYMMDD
    print("올바른 생년월일이 아닙니다.")
#윤년을 판별하는 함수
def Leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False
    
def main():
    mlist = [1,3,5,7,8,10,12] #31일이 있는 달
    
    inputString = input("생년월일을 입력하시오:")
    
    if(len(inputString)!=8): #YYYYMMDD형식 아니면 wrong
        Wrong()
    else:
        year = int(inputString[0:4])#0~3, 리스트를 정수로 변환
        month = int(inputString[4:6])#4~5
        date = int(inputString[6:])#6~끝
        
        if(year<1):
            Wrong()
        elif(month>12 or month<1):
            Wrong()
        #31일 있는 달
        elif(month in mlist and (date>31 or date<1)):
            Wrong()
        #30일까지 있는 달
        elif(month !=2 and month not in mlist and (date>30 or date<1)):
            Wrong()
        #윤년 아니면 28일까지, 윤년이면 29일까지
        elif(month==2 and (Leap(year)==False and (date>28 or date<1)) or ((Leap(year)==True and (date>29 or date<1)))):
            Wrong()

        else:
            print("올바른 생년월일입니다.")
main()