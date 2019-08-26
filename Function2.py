#p107
import random
# n = random.randint(1, 6) #1부터 6까지의 정수 중에 하나를 뽑는다.
# print("6면 주사위 굴린 결과 : ", n)
# n = random.randint(1, 6)
# print("6면 주사위 굴린 결과 : ", n)
# n = random.randint(1, 6)
# print("6면 주사위 굴린 결과 : ", n)

# def rolling_dice():
#     n = random.randint(1, 6)
#     print("6면 주사위 굴린 결과 : ", n)
# rolling_dice()
# rolling_dice()

# #p109
# def star():
#     print("*"*5)

# star() #*****
# star() #*****
# star() #*****

# def rolling_dice():
#     n = random.randint(1, 6)
#     print("6면 주사위 굴린 결과 : ", n)

# #p110
# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip,"면 주사위 굴린 결과 : ", n)

# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(8)
# rolling_dice(10)
# rolling_dice(12)
# rolling_dice(20)


#p112
# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip,"면 주사위 굴린 결과 : ", n)

# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip)
#         print(pip,"면 주사위 굴린 결과 : ", r," : ", n)

# rolling_dice(6, 1)
# rolling_dice(6, 2)
# rolling_dice(12, 0)
# rolling_dice(20, -3)

#p113
# print("♡")
# print("♡","♪")
# print("♡","♪","♣")
# print("♡","♪","♣","♠")
# print("♡","♪","♣","♠","★")

# def p( *args ):
#     str = ""
#     for a in args:
#         str = str + a
#     print(str)

# print("♡")
# print("♡","♪")
# print("♡","♪","♣","♠")

# def p( space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)

# print(",",3,"♡","♪")
# print("☆",2,"♡","♪","♣")
# print("_",3,"♪","♣","♠")

#p115
# def star2( ch , *args):
#     # str = args[0]
#     # for i in range(1, len(args)):
#     #     str = (space * space_2) + args[i]
#     #     print(str) 
#     for i in range(len(args)):
#         star2("♪", 3)
#         star2("♡", 1, 2, 3)

#p117
# def fn(a,b, c, d, e):
#         print(a, b, c, d, e)

#p118
#star 함수 정의
# def star(mark, repeat, space, space_repeat, line):
#         for i in range(1, line):
#                 #str = " "
#                 # for j in range(2, repeat):
#                 str += (mark * repeat) + (space * space_repeat) + (mark * space_repeat)  
#         print(str)

# star("*", 3, "_", 2, 3)

#p119
# def hello(msg = "안녕하세요"):
#         print(msg + "!")

# hello("하이")
# hello("hi")
# hello()

# #p120
# def hello2(name, msg = "안녕하세요"):
#         print(name+ "님, " + msg + "!")

# hello2("김재환", "오랜만이에요")
# hello2("장원이")
# # hello2() #name 없음

# def fn2(a, b = []): #list의 경우에는 
#         b.append(a)
#         print(b)

# fn2(3)
# fn2(5)
# fn2(10)

#p123
# def gugudan(dan = 2):
#         for i in range(1, 9+1):
#                 print(dan , "X" , i , " = " , dan*i)
# #String끼리는 +를 사용 가능
# #print(str(dan) , "X" , str(i) , " = " , str(dan*i)
# gugudan(3)
# gugudan(2)
# gugudan() #인자 없음

#p125
# def sum(*numbers):
#         sum_value = 0
#         for number in numbers:
#                 sum_value += number

#         return sum_value

# print("1 + 3 = ", sum(1,3))
# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

# def min(*numbers):
#         min_value = numbers[0]
#         for number in numbers:
#                 if min_value > number:
#                         min_value = number
#         return min_value

# print("min(3, 6, -2) = ", min(3, 6, -2))

def max(*numbers):
        max_value = numbers[0]
        for number in numbers:
                if max_value < number:
                        max_value = number
        return max_value

print("max(8, 1, -1, 12) = ", max(8, 1, -1, 12))


def multi_num(multi, start, end):
        result = []
        for n in range(start, end):
                if n % multi:
                        result.append(n)
        return result

print("nulti_num(17, 1, 200) = ", multi_num(17, 1, 200))
print("multi_num(3, 1, 100) = ", multi_num(3, 1, 100))

def min_max(*args):
        min_value = args[0]
        max_value = args[0]
        for a in args:
                if min_value > a:
                        min_value = a   
                if max_value < a:
                        max_value = a
        return min_value, max_value

(min, max) = min_max(52, -3, 23, 89, -21)
print("최솟값 : ", min , "최댓값 : ", max)
                