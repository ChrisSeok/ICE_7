#5번문제. C111061 박서연

length = int(input("문자열의 길이를 입력하시오 : "))

if length % 2 == 0:
    palindrome = 26**(length//2)

else:
    palindrome = 26*26**((length-1)//2)
    
print("전체 가능한 소문자 알파벳 문자열", 26**length, "개 중 회문의 개수는", palindrome, "개입니다.")