# 4번_B735042_김대겸

# 주어진 문자열을 뒤집어 출력하는 함수 reversepro(x)선언.
def revesepro(x):
    result = "" # 뒤집은 결과를 저장할 빈 문자열 result
    for i in x: 
        result = i + result # 입력된 문자열의 문자를 하나씩 꺼내어 빈문자열에 순서대로 저장.
    print(result) # 결과 result 출력.

userInput = input("문자열을 입력하시오: ") # 사용자로부터 문자열 입력받기
revesepro(userInput) # reversepro(x) 호출
