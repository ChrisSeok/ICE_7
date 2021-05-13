#2번, B835193 석채원
def main():
    instr = input("문자열을 입력하시오: ")
    inletter = input("문자를 입력하시오:")
    count = 0
    for i in instr:
        if(i==inletter):
            count+=1
    print("\"%s\" 문자의 빈도는 %d 이다"%(inletter,count))
main()        
