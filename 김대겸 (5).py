# 5번_B735042_김대겸

# 회문의 개수를 출력하는 함수 palinD(x)선언.
def palineD(x):
    alphaChar = [] # 소문자 알파벳을 저장할 빈 리스트
    for i in range(97, 123): # 아스키 코드를 이용하여 alphaChar에 소문자 알파벳들을 모두 저장.
        alphaChar.append(chr(i))
    totalStr = len(alphaChar)**(x)  # 전체 가능한 소문자 문자열의 수
    palineStr = 0 # 회문의 수를 저장할 변수 palineStr
    if x % 2 == 0: # 문자열의 길이가 짝수일 때.
        palineStr = len(alphaChar)**(x//2)
    elif x % 2 == 1: # 문자열의 길이가 홀수일 때.
        palineStr = len(alphaChar)**((x//2) + 1)
    print("전체 가능한 소문자 알파벳 문자열", totalStr, "개 중 회문의 개수는", palineStr,"개입니다.")

palineD(3)