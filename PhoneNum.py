
# name = str(input("찾고 싶은 전화번호의 일부를 입력하시오 : "))
# list(name == Num)

print("< 전화번호부 >")
Num =  [
       {" 장원이 : 010-9483-0984"},
       {"김재환 : 010-1996-0527"},
       {"강혜정 : 010-2002-0504"}
]
find = input("찾으실 분의 이름을 입력하세요 : ") 
for name in Num:
    if find in name:
        print(name, "님의 전화번호는 ",Num[name],"입니다.")

