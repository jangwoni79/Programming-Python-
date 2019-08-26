num = input("숫자를 입력하시오 : ")

sum = 0

for i in num: #2317을 입력하면 '2','3','1','7'로 쪼개져서 나옴
    sum+=int(i)
print(sum)