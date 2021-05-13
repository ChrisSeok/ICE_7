#3번 c111152 임종욱

def main():
    dial = dict(zip(['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYW'],[2,3,4,5,6,7,8,9]))
    st = input('문자열을 입력하시오: ')
    for i in st:
        for x in dial:
            if i in x:
                print(dial[x],end = '')
                break
main()