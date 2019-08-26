#p142 gugudan.py
def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 9+1):
        print(n, "+", i, "=", n*i)

if __name__=='__main__': #자기 모듈 실행하면 실행되고, 다른데서 import하면 실행 안됨!
        gugudan(3)