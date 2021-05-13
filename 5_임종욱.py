#5번 c111152 임종욱

def main():
    Len = int(input('문자열의 길이를  입력하시오: '))
    palindrome(Len)
    #회문 검사하는 함수
    # 회문수는 i 가 짝수이면 26^(i/2) i가 홀수이면 26^(i//2 +1)
def palindrome(i):
    Num_st = 26**i
    if i % 2 == 0:
        Num_pal = 26**(i/2)
    else :
        Num_pal = 26**(i//2 + 1)
    print('전체 가능한 소문자 알파벳 문자열',Num_st,'개 중 회문의 개수는 '+str(Num_pal)+'개입니다.')

main()