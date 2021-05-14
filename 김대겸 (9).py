#9번_B735042_김대겸

def pbAdd(): #입력모드
    global dicName #전역변수 선언
    global dicNumber 
    dicName = {} # 이름을 저장할 빈 딕셔너리 선언.
    dicNumber = {} # 번호를 저장할 빈 딕셔너리 선언.
    while True: # 무한루프로 시작
        name = input("이름? ") #사용자로부터 이름을 입력받음.
        if name == '':    #사용자가 엔터키를 입력하면
            print()
            print("중복되지 않는 사람 수 :", len(dicName.keys()))
            print("중복되지 않는 전화번호 수 :", len(dicNumber.keys()))
            print()
            pbClear() #검색모드 호출
            break     # 호출 후 pbAdd() 종료
        else:                  #엔터키가 아니라면
            while True: #무한루프로 시작
                number = input("전화번호? ") #사용자로부터 번호를 입력받음
                if number != '':             #number가 엔터키가 아니라면
                    break                     #무한루프 종료
            if name in dicName.keys(): #만약 name이 이미 저장되어 있다면
                dicName[name].append(number) #dicName의 key name의 list형태의 value에 number를 추가
                dicNumber[number].append(name) #dicNumber의 key number에 list형태의 value에 name추가
            else:               #만약 name이 저장되어 있지 않다면
                dicName[name] = list() #dicName의key name의 value에 빈 리스트를 만들고
                dicName[name].append(number)  #number을 추가
                dicNumber[number] = list() #dicNumber의 key number의 빈 리스트를 만들고
                dicNumber[number].append(name) #name을 추가

def pbClear():  #지우기모드
    while True: #무한루프로 시작
        infor = input("지우고싶은 사람의 이름 또는 전화번호를 입력하세요?")
        if infor == '':  #엔터키 입력시 프로그램 종료
            print("프로그램을 종료합니다.")
            break
        elif infor[0] in '0123456789': #infor가 전화번호일때
            if infor in dicNumber:      #dicNumber에 저장된 전화번호라면
                del dicNumber[infor]     #dicNumber에서 그 번호를 key로 가지는 key와 value 삭제
                for k in list(dicName): #dicName의 Key중에서 Key를 하나씩 꺼내어
                    if infor in dicName[k]: #key의 value에 infor가 있다면
                        dicName[k].remove(infor)
                    if len(list(dicName[k])) == 0:              #만약 value의 개수가 0이라면
                        del dicName[k]                     #그 key를 제거
                print("중복되지 않는 전화번호 수 :", len(dicNumber.keys()))
                for i in dicNumber.keys():
                    print(i, end=' ')
                print()
            else:                       #저장되지 않은 전화번호라면
                print(infor, "는 등록되지 않았습니다.")
        else:                          #infor가 이름일때
            if infor in dicName:        #dicName에 저장된 이름이라면
                del dicName[infor]       #dicName에서 그 번호를 key로 가지는 key와 value 삭제
                for k in list(dicNumber): #dicNumber의 key중에서 key를 하나씩 꺼내어
                    if infor in dicNumber[k]: #key의 value에 infor가 있다면
                        dicNumber[k].remove(infor) #key k의 value를 하나씩 꺼내어
                    if len(list(dicNumber[k])) == 0:              #만약 value의 개수가 0이라면
                        del dicNumber[k]                      #그 key를 제거
                print("중복되지 않는 사람의 수 :", len(dicName.keys()))
                for i in dicName.keys():
                    print(i, end=' ')
                print()
            else:                       #저장되지 않은 이름이라면
                print(infor, "은 등록되지 않았습니다.")
# pbAdd()호출
pbAdd()


