# 6번_B735042_김대겸

def phoneBook(): 
    dicbook = {} # 이름과 전화번호를 저장할 빈 딕셔너리 선언.
    while True: # 무한루프로 시작
        name = input("이름? ") # 사용자로부터 이름을 입력받음.
        if name not in dicbook: # 저장되어 있지 않은 이름일 때
            if name == '':      # 사용자가 엔터키를 입력하면
                print("프로그램을 종료합니다.") # 프로그램 종료
                break 
            number = input("전화번호? ") # 엔터키가 아니라면 사용자로부터 전화번호를 입력받는다.
            dicbook[name] = number # 딕셔너리에 키값에 해당하는 이름과 value에 해당하는 전화번호 저장
        elif name in dicbook: # 저장되어 있는 이름일 때
            wantname = name # 찾는 이름은 사용자가 입력한 이름
            wantnum = dicbook[wantname] # 찾는 번호는 wantname의 value
            print(wantname, "의 전화번호는", wantnum, "입니다.")
        
# phonBook()호출.
phoneBook()

