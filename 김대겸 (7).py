# 7번_B735042_김대겸

def phoneBook2(): 
    dicbook = {} # 이름과 전화번호를 저장할 빈 딕셔너리 선언.
    while True: # 무한루프로 시작
        userInput = input("이름 또는 전화번호? ") #사용자로부터 이름 또는 전화번호를 입력받음.
        if userInput == '':                #사용자가 엔터키를 입력하면
            print("프로그램을 종료합니다.")    #프로그램 종료
            break
        #1.사용자가 전화번호를 입력했을 때
        if userInput[0] in '0123456789':  
            if userInput not in dicbook.values(): #저장되지 않은 전화번호이면
                print("없는 전화번호입니다.")
            elif userInput in dicbook.values(): #저장되어 있는 전화번호 일때
                wantnum = userInput 
                for k in dicbook.keys(): #dicbook의 key 중에서 
                    if dicbook[k] == wantnum: #key에 해당하는 value가 wantnum과 같다면 
                        wantname = k     #wantname은 그 키가 된다.
                print("전화번호", wantnum, "의 소유주는", wantname)
        #2.사용자가 이름을 입력했을 때               
        else: 
            if (userInput not in dicbook): # -저장되어 있지 않은 이름일 때 
                while True:                   #엔터키가 아니라면 무한루프로 시작
                    number = input("전화번호? ") #사용자로부터 전화번호를 입력받는다.
                    if number != '':             #입력받은 전화번호가 엔터키가 아니라면
                        break                     #무한루프 종료.
                #딕셔너리에 키값에 해당하는 이름과 value에 해당하는 전화번호를 integer 형태로 저장
                dicbook[userInput] = number 
            elif userInput in dicbook:       # -저장되어 있는 이름일 때
                wantname = userInput          #찾는 이름은 사용자가 입력한 이름
                wantnum = dicbook[wantname]    #찾는 번호는 wantname의 value
                print(wantname, "의 전화번호는", wantnum, "입니다.")
        
# phonBook()호출.
phoneBook2()

