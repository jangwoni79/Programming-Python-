#학번 입력 받아 학과 출력하기 #예 : "2320"을 입력하면, "뉴미디어 웹솔루션과"를 출력

# print("학번을 입력하시오 : ")
# int n = input()

# sn = input("학번을 입력하시오 : ")
# g = sn[0]
# c = sn[1]

# if g == "1" or g == "2":
#     if c =="1" or c == "2":
#         print("뉴미디어소프트웨어과")
#     elif c == "3" or c == "4":
#         print("뉴미디어웹솔루션과") 
#     elif c == "5" or c == "6":
#         print("뉴미디어 디자인과")
# elif g == "3":
#     if c == "1" or c == "2":
#         print("인터랙티브미디어과")
#     elif c == "3" or c == "4":
#         print("뉴미디어 디자인과")
#     elif c == "5" or c == "6":
#         print("뉴미디어솔루션과")

# m12학년 = ["뉴미디어소프트웨어과", "뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어웹솔루션과", "뉴미디어디자인과", "뉴미디어디자인과"]
# m3학년 = ["인터랙티브미디어과", "인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어디자인과", "뉴미디어솔루션과", "뉴미디어솔루션과"]

# sn = input("학번을 입력하시오 : ")
# g = sn[0]
# g = int(g)
# c = sn[1]
# c = int(c)
# if g == 1 or g == 2:
#     print(m12학년[c-1])
# elif g == 3:
#     print(m3학년[c-1])

# m = [
#     ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"] , 
#     ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"] ,
#     ["인터랙티브미디어과",  "뉴미디어디자인과", "뉴미디어솔루션과"]
# ]
# sn = input("학번을 입력하시오 : ")
# g = sn[0]
# g = int(g)
# c = sn[1]
# c = int(c)
# print(m[g - 1][(c - 1) // 2])

m = [
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"] , 
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"] ,
    ["인터랙티브미디어과",  "뉴미디어디자인과", "뉴미디어솔루션과"]
]

sn = input("학번을 입력하시오 : ")

g = sn[0]
g = int(g)
c = sn[1]
c = int(c)
print(m[g - 1][(c - 1) // 2])