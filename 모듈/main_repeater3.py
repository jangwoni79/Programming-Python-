import repeater as r

s = input("반복할 분자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")
r.repeat(s,int(n))
r.repeat(s)
r.once(s)