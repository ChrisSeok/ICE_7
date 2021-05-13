#4번, B835193 석채원
def main():
    instr = input("문자열을 입력하시오:")
    newstr = ''
    for i in instr:
        newstr=i+newstr
    print(newstr)
main()
