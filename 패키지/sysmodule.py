import sys
print("실행 파일명 : ", sys.argv[0]) #입력하지 않더라도 기본적으로 실행
for i in range(1, len(sys.argv)): #1부터 argv의 길이만큼 출력
    print("옵션", i, ":", sys.argv[i])

sys.exit()

for i in range(1, 100):
    print("여기는 실행되지 않습니다.")