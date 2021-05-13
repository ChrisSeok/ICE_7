#8번, B835193 석채원
phonebook = list()
phnameset = set()
phnumset = set()
#문자열이 숫자로 이루어졌는지 판별하는 함수
def digit(input):
    numlist = ['0','1','2','3','4','5','6','7','8','9']
    count = 0
    for i in input:
        if(i not in numlist):
            count+=1
    if(count==0):
        return True #모두 숫자면 참을 리턴
    else:
        return False
#이름과 전화번호 입력받아 저장하는 함수   
def inputbook():
     while 1:
        name = input("이름?")
        #엔터키 입력될 경우 종료
        if(name == ''):
            return
        else:
            while 1:
                phnum = input("전화번호?")
                if(digit(phnum)==True and phnum!=''):
                    break
            phonebook.append([name,phnum])
            phnameset.add(name)
            phnumset.add(phnum)
#중복되지 않는 사람,전화번호 수 출력하는 함수
def printdata():
    print("중복되지 않는 사람 수:%d"%(len(phnameset)))
    print("중복되지 않는 전화번호 수:%d"%(len(phnumset)))
#검색하는 함수
def searchbook():
    while 1:
        count = 0
        inputstr = input("찾고싶은 사람의 이름 또는 전화번호를 입력하세요?")
        if(inputstr == ''):
            print("프로그램을 종료합니다.")
            return
        else:
            if(digit(inputstr)==False): #입력이 이름일 경우
                #전화번호부에 존재하는 이름
                for i in range(len(phonebook)):
                    if(phonebook[i][0]==inputstr):
                        print(phonebook[i][1],end=' ')
                        count+=1
                
            else: #입력이 숫자일 경우
                for i in range(len(phonebook)):
                     if(phonebook[i][1]==inputstr):
                        print(phonebook[i][0],end=' ')
                        count+=1
            print()   
        #전화번호부에 존재하지 않는 이름
        if(count==0):
            print(inputstr,"는 등록되지 않았습니다.")    
    
def main():
   inputbook()
   printdata()
   searchbook()
           
main()