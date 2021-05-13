#3번, B835193 석채원
def main():
    #입력은 대문자만 가정
    list = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
    instr = input("문자열을 입력하시오:")
    num = ''
    for i in instr: #입력된 문자열 순회
        for j in range(8): #리스트 원소 7개 순회
            if(i in list[j]):
                num+=str(j+2) #다이얼에 맞추어 +2 해준다
    print(num)
main()
            
