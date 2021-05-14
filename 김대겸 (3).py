# 3번_B735042_김대겸

# 사용자로부터 문자열 입력받기
inputUser = input("문자열을 입력하시오: ")
# 각 알파벳들에 해당하는 숫자를 값으로 가지는 딕셔너리 생성
numStr = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
result = "" # 결과를 저장할 빈 문자열 생성
for i in inputUser: # 사용자로부터 입력받은 문자열을 하나씩 꺼내어
    for x in numStr.keys(): # 딕셔너리numstr의 key를 요소로 가지는 리스트에서 꺼낸 key에서
        if i in x:          # 만약 i가 key x에 있다면
            result = result + str(numStr[x]) # 빈문자열 result에 key x에 해당하는 값을 추가
# result출력
print(result)
