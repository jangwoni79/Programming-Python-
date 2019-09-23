# f = open("file.txt","r")
#
# text = f.read()
# print(text)
#
# f.close()

f = open("file.txt", "r", encoding = "utf8") #r : read text

text0 = f.readline() # \n까지 읽기
print(text0)
text1 = f.readline()
print(text1)
text2 = f.readline()
print(text2)

f.close()