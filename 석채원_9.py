#9번, B835193 석채원
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
#삭제하는 함수
def delete():
    dellist = list()
    while 1:
        indel = input("지우고 싶은 사람의 이름 또는 전화번호를 입력하세요?")
        if(indel==''):
            return
        elif(digit(indel)==False):#입력이 이름
            if(indel in phnameset):
                phnameset.remove(indel)
                print("중복되지 않는 사람 수:%d"%(len(phnameset)))
                for i in phnameset:
                    print(i,end=' ')
                print()
            #phonebook 에서 해당 리스트 삭제
            #지운 이름들에 해당하는 번호가 phonebook에 또 있지 않는 한 phnumset세트에서 삭제
            for i in range(len(phonebook)):
                if(phonebook[i][0]==indel):
                    dellist.append(i)
            for j in dellist[::-1]: #역순으로 순회해야 인덱싱 오류가 안난다(삭제하기 때문에 리스트인덱스 바뀜)
                q=j
                count = 0
                ph = phonebook[q][1]
                del phonebook[j]
                for k in range(len(phonebook)):
                    if(phonebook[k][1]==ph):
                        count+=1
                if(count==0):
                    phnumset.remove(ph)
            dellist.clear()
            print(phonebook)
                   
        else: #입력이 숫자
            if(indel in phnumset):
                phnumset.remove(indel)
                print("중복되지 않는 전화번호 수:%d"%(len(phnumset)))
                for i in phnumset:
                    print(i,end=' ')
                print()
            for i in range(len(phonebook)):
                if(phonebook[i][1]==indel):
                    dellist.append(i) #for문을 도는 중 삭제하면 index가 꼬인다
            #번호는 지워지고 이름만 phnameset에 남겨져있는것들 삭제
            #전화번호부에서 해당 리스트 삭제
            for j in dellist[::-1]:
                count = 0
                nm = phonebook[j][0]
                del phonebook[j]
                for k in range(len(phonebook)):
                    if(phonebook[k][0]==nm):
                        count+=1
                if(count==0):
                    phnameset.remove(nm)
            dellist.clear()
            print(phonebook)
 
#검색하는 함수
def searchbook():
    print(phonebook)
    print("검색모드로 넘어갑니다.")
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
    print(phonebook)
    delete()
    searchbook()
           
main()
