# 2번_B735042_김대겸

# 문자열 x에서 문자 y의 개수를 세는 countUser(x, y) 선언.
def countuUser(x, y):
    result = x.count(y)
    print('"',y ,"\"문자의 빈도는 ", result, "이다.")

#사용자로부터 문자열과 찾고싶은 문자를 입력받기
a = input("문자열을 입력하시오: ")
b = input("문자를 입력하시오: ")

# 함수counUser(x, y)호출
countuUser(a, b)


