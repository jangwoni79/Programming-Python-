import repeater

s = input("반복할 분자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")
n = int(n)
repeater.repeat(s,int(n))
repeater.repeat(s)
repeater.once(s)