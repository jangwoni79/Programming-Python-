#239
import pickle
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : ", self.name + "\n나이 : " + str(self.age))

f = open("person_data.bin", "wb")

p = Person("장원이", 18)

pickle.dump(p, f) #p객체를 f파일로 내맘속에 저장
f.close()

# #load
# #p247
# f = open("person_data.bin", "rb")
# person1 = pickle.load(f)
# f.close()
# print(person1)

#p240
p1 = Person("이은상", 18)
p2 = Person("김재환", 24)
p3 = Person("박지민", 25)
people = [p1, p2, p3]
f = open("people_data.bin", "wb")
pickle.dump(people, f)
f.close()

#load object list
#p247
f= open("people_data.bin", "rb")
peo = pickle.load(f)
f.close()
for p in peo:
    print(p)

sum = 0
for p in peo:
    sum+= p.age
print(sum)
