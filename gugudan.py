
# #2단 출력
# for i in range(1, 9+1):
#     print("2 x {} = {}".format(i, 2*i))

# #2 ~ 5단 출력
# for i in range(1, 9+1):
#     print("2 x {} = {}".format(i, 2*1))
# for i in range(1, 9+1):
#     print("3 x {} = {}".format(i, 3*1))
# for i in range(1, 9+1):
#     print("4 x {} = {}".format(i, 4*1))
# for i in range(1, 9+1):
#     print("5 x {} = {}".format(i, 5*1))

# for dan in range(2, 9+1):
#     for i in range(1, 9+1):
#         print("{} x {} = {}".format(dan, i, dan*i))
#     print("------------")

# for dan in range(2, 9+1):
#     for i in range(1, 9+1):
#         if i > 7:
#             break
#         print("{} x {} = {}".format(dan, i, dan*i))
#     print("------------")

for dan in range(2, 9+1):
    for i in range(1, 9+1):
        if i > 7:
            break
        if i%2 == 0:
            continue
        print("{} x {} = {}".format(dan, i, dan*i))
    print("------------")