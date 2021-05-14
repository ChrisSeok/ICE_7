#4번문제. C111061 박서연 

string = str(input("문자열을 입력하시오: "))
re_string = ""

for i in string:
    re_string = i + re_string

print(re_string)