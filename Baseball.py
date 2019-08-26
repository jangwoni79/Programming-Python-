#야구게임
#3자리 중복없는 임의의수 만들자
#무한반복
#사용자 입력을 받자
#strike, ball 판정
#사용자 입력, strike, ball 출력하기
#임의의수랑 사용자 입력이 같으면 hit, break
import random
# random.shuffle(list(range(1, 9+1))
# l = list(range(1, 9+1))
# ''.join(str(i) for i in l[:3])
# l[:3]
# a = ""
# for i in l[:3]:
#     a+=str(i)

l = random.sample(range(1, 9+1), 3)
computer = ''.join(str(i) for i in l)


# computer = "851"
while True:
    player = input("숫자 세자리 맞추기 : ")
    strike = 0
    ball = 0
    #strike, ball 판정
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    print(player, " strike : " , strike, " ball : ", ball)
    if computer == player:
        print("HIT")
        break