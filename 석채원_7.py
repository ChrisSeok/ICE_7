#7번, B835193 석채원
phonebook = dict()
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
        
def main():
    while 1:
        inputstr = input("이름 또는 전화번호?")
        #엔터키 입력될 경우 종료
        if(inputstr == ''):
            print("프로그램을 종료합니다")
            return
        #입력이 숫자일 경우 
        elif(digit(inputstr)):
            if(inputstr in phonebook.values()): #이미 phonebook에 있으면 이름 출력
                name = [k for k, v in phonebook.items() if v == inputstr]
                print(inputstr,"의 소유주는",name[0]) #name을 출력하면 리스트 형태로 나오기 때문에
            else:
                print("없는 전화번호입니다.")
        #입력이 문자일 경우
        else:
            if(inputstr in phonebook.keys()):#이미 phonebook에 있으면 전화번호 출력
                print(inputstr,"의 전화번호는",phonebook.get(inputstr))#get내장함수:key로만 서치 가능
            else:
                #이미 저장돼있지 않으면 전화번호 입력받아 딕셔너리에 저장
                while 1:
                    phnum = input("전화번호?")
                    #숫자일 경우에만 무한루프 break
                    if(digit(phnum)):
                        break
            phonebook[inputstr] = phnum
           
main()