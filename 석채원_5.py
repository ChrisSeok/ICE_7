#5번, B835193 석채원
def main():
    inlen = int(input("문자열의 길이를 입력하시오: "))
    #짝수일 경우
    if(inlen%2==0):
        palnum = 26**(inlen/2)
    #홀수일 경우
    else: 
        palnum = 26**((inlen//2)+1)#중간문자 고려
    allnum = 26**inlen
    print("전체 가능한 소문자 알파벳 문자열 %d개 중 회문의 개수는 %d개입니다."%(allnum,palnum))

main()