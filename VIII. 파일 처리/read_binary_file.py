#p245
import array

f = open("data.bin", "rb")
data = f.read()
for item in data:
    print(item, end = ", ")
f.close()