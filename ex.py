class Contact:  #Contact 클래스 정의

   def __init__(self, error, read, answer): #생성자 함수
        self.error = error
        self.read = read
        self.answer = answer
   def print_info(self): #정보 출력 함수
        print("Error : ", self.error)
        print("Read : ", self.read)
        print("Answer : ", self.answer)
        print()
   

def set_contact():  
   error = input("Error : ")
   read = input("Read : ")
   answer = input("Answer : ")
   contact = Contact(error, read, answer)
   #입력한 변수들을 클래스의 인스턴스에 넣어서 초기화
   #순서를 바꾸면 안 된다. contact 객체에 넣고 return한다. 
   #main함수에 없는 이유는 재사용성을 높이기 위해서. 
   return contact

def print_menu():   #메뉴 출력
    print("")
    print("!!프로그래밍 언어를 선택해 주세요!!")
    print("▶ 보기 ◀")
    print("1. JAVA")
    print("2. Python")
    print("3. JSP")
    print("4. error 추가")
    print("5. 저장")
    print("5. 종료")
    print("")
    menu = input("메뉴 선택 : ")
    return int(menu) #입력 시 문자열로 들어가기 때문에 int로 바꿔줌

def print_menu4(): #메뉴4번의 추가 메뉴
    print("")
    print("!!추가하고 싶은 프로그래밍 언어를 선택해 주세요!!")
    print("▶ 보기 ◀")
    print("1. JAVA")
    print("2. Python")
    print("3. JSP")
    print("4. 종료")
    menu4 = input("메뉴 선택 : ")
    return int(menu4)

def print_java(java_list):    #주소록 정보가 출력된다. contact_list를 받아서 for 문으로 돌린다.
   for contact in java_list:
         contact.print_info()   #출력한다.
       
def print_python(python_list): #주소록 정보가 출력된다. contact_list를 받아서 for 문으로 돌린다.
   for contact in python_list:
         contact.print_info()   #출력한다.
       
def print_jsp(jsp_list):    #주소록 정보가 출력된다. contact_list를 받아서 for 문으로 돌린다.
   for contact in jsp_list:
         contact.print_info()   #출력한다.

def store_java_fwrite(java_list):
   #파일을 열고 써야되니까 wt. 텍스트모드로 쓴다.
   #4줄씩 읽으니까 4줄씩 해야된다. 
   f = open("java_db.txt", "wt")
   for contact in java_list:
#   contact는 객체로 받는다는 소리. 반복하는데 그 변수가 객체다. 
#   개행을 각자 넣어줘야 한다.
       f.write(contact.error + '\n')
       f.write(contact.read + '\n')
       f.write(contact.answer + '\n')
   f.close()

def store_python_fwrite(python_list):
# 파일을 열고 써야되니까 wt. 텍스트모드로 쓴다.
   #4줄씩 읽으니까 4줄씩 해야된다. 
   f = open("PythonS/python_db.txt", "wt")
   for contact in python_list:
#   contact는 객체로 받는다는 소리. 반복하는데 그 변수가 객체다. 
#   개행을 각자 넣어줘야 한다.
       f.write(contact.name + '\n')
       f.write(contact.phone_number + '\n')
       f.write(contact.e_mail + '\n')
       f.write(contact.addr + '\n')
   f.close()

def store_jsp_fwrite(jsp_list):
# 파일을 열고 써야되니까 wt. 텍스트모드로 쓴다.
   #4줄씩 읽으니까 4줄씩 해야된다. 
   f = open("PythonS/jsp_db.txt", "wt")
   for contact in jsp_list:
#   contact는 객체로 받는다는 소리. 반복하는데 그 변수가 객체다. 
#   개행을 각자 넣어줘야 한다.
       f.write(contact.name + '\n')
       f.write(contact.phone_number + '\n')
       f.write(contact.e_mail + '\n')
       f.write(contact.addr + '\n')
   f.close()

def load_java_fwrite(java_list):
   f = open("PythonS/contact_db.txt", "rt")
#   readlines()는 모든 행을 저장한다. 5명이면 20줄이 저장된다. 
   lines = f.readlines()   #lines에는 리스트가 들어간다. 총 4개. 개행까지 포함한 문자열로.
   num = len(lines) / 4    # 4 / 4인데 나누면 float연산이 된다. 1.0이 나와서 num에는 1.0이 들어간다. 
   num = int(num)          # 1.0을 정수로 고쳐주기 위해서 int를 써준다.
   
   #주소록의 개수만큼 돌아라. 
   for i in range(num):
       error = lines[4*i].rstrip('\n')  #rstrip은 맨 오른쪽의 문자를 없앤다는 뜻. 즉, 개행을 없앤다. \n을 지워주기 위해서.
       #왜? 데이터 안에 개행이 있으면 안 되니까. 나중에 출력할 때 줄바꿈이 더 되기도 하고. 
       # 만약에 중간에 개행이 있다면 replace를 써줘야 한다. 
       read = lines[4*i+1].rstrip('\n')
       answer = lines[4*i+2].rstrip('\n')
       contact = Contact(error, read, answer)
       java_list.append(contact)
   f.close()

def store_java_print(java_list):
   f = open("PythonS/java_db.txt", "wt")
   for contact in java_list:
#       print는 가변인자라서 여러 변수를 써도 된다. contact를 하나씩 빼온다. 한 행 안의 파일이 ,로 구분되어 있는 파일(cvs), sep의 default는 ' ' end의 디폴트는
#       'n'이고 파일에 저장해야 하니까 file=f.
       print(contact.error, contact.read, contact.answer, file=f, sep=',')
   f.close()

def load_java_print(java_list):   #얘네들은 call by reference이다. contact_list.append이니까. 이 라인에 있는 파라미터(contact_list)에 가서 넣는 것이다.
   f = open("PythonS/java_db.txt", "rt")
   lines = f.readlines() #readlines는 모든 행을 다 읽는데 리스트로 들어가서 ['ㅁ,ㄴ,ㅇ,ㄹ', 'ㅁ,ㄴ,ㅇ,ㄹ',]이런 식...''안에는 문자열이다. 
   for line in lines:  #lines 리스트 안에 있는 만큼 line을 실행. line도 리스트가 된다. 
       data = line.split(',')  #구분 기호를 집어넣는다. split은 기본이 공백이다. Line이 리스트니까 공백을 구분 단위로 한다. 
       contact = Contact(data[0], data[1], data[2])   #0번째는 이름, 1번째는 전화번호... 칼럼이 늘어나면 그대로 다시 넣어줘야 한다. 
       java_list.append(contact)

   f.close()

def store_java_pickle(java_list):
   f = open("PythonS/java_db.data", "wb")   #바이너리 파일로 불러올 때는 확장자도 바꿔줘야 한다.
   import pickle #굳이 맨 위에 정의하지 않아도 된다. 
   pickle.dump(java_list, f)    #꺼내서 하나하나씩 저장할 필요가 없다. 리스트 통째로 저장한다.
   f.close()

def load_java_pickle():  #파라미터가 굳이 필요없다. call by value처럼 동작하기 때문에
   f = open("PythonS/java_db.data", "rb")
   import pickle
   java_list = pickle.load(f)   # 통째로 받아와서 다시 저장한다. .을 안 찍고 =으로 받기 때문에 이전 게 사라지고 새로운 객체가 들어온다.
#   객체 형태로 모두 들어간다. 리스트형태로 모두 들어간다. 
   f.close()
   return java_list #왜 굳이 return을 해야될까? 객체니까 contact_list의 주소값을 전달해준다. 

def load_python_fwrite(python_list):
   f = open("PythonS/python_db.txt", "rt")
#   readlines()는 모든 행을 저장한다. 5명이면 20줄이 저장된다. 
   lines = f.readlines()   #lines에는 리스트가 들어간다. 총 4개. 개행까지 포함한 문자열로.
   num = len(lines) / 4    # 4 / 4인데 나누면 float연산이 된다. 1.0이 나와서 num에는 1.0이 들어간다. 
   num = int(num)          # 1.0을 정수로 고쳐주기 위해서 int를 써준다.
   
   #주소록의 개수만큼 돌아라. 
   for i in range(num):
       error = lines[4*i].rstrip('\n')  #rstrip은 맨 오른쪽의 문자를 없앤다는 뜻. 즉, 개행을 없앤다. \n을 지워주기 위해서.
       #왜? 데이터 안에 개행이 있으면 안 되니까. 나중에 출력할 때 줄바꿈이 더 되기도 하고. 
       # 만약에 중간에 개행이 있다면 replace를 써줘야 한다. 
       read = lines[4*i+1].rstrip('\n')
       answer = lines[4*i+2].rstrip('\n')
       contact = Contact(error, read, answer)
       python_list.append(contact)
   f.close()

def store_python_print(python_list):
   f = open("PythonS/python_db.txt", "wt")
   for contact in python_list:
#       print는 가변인자라서 여러 변수를 써도 된다. contact를 하나씩 빼온다. 한 행 안의 파일이 ,로 구분되어 있는 파일(cvs), sep의 default는 ' ' end의 디폴트는
#       'n'이고 파일에 저장해야 하니까 file=f.
       print(contact.error, contact.read, contact.answer, file=f, sep=',')
   f.close()

def load_python_print(python_list):   #얘네들은 call by reference이다. contact_list.append이니까. 이 라인에 있는 파라미터(contact_list)에 가서 넣는 것이다.
   f = open("PythonS/python_db.txt", "rt")
   lines = f.readlines() #readlines는 모든 행을 다 읽는데 리스트로 들어가서 ['ㅁ,ㄴ,ㅇ,ㄹ', 'ㅁ,ㄴ,ㅇ,ㄹ',]이런 식...''안에는 문자열이다. 
   for line in lines:  #lines 리스트 안에 있는 만큼 line을 실행. line도 리스트가 된다. 
       data = line.split(',')  #구분 기호를 집어넣는다. split은 기본이 공백이다. Line이 리스트니까 공백을 구분 단위로 한다. 
       contact = Contact(data[0], data[1], data[2])   #0번째는 이름, 1번째는 전화번호... 칼럼이 늘어나면 그대로 다시 넣어줘야 한다. 
       python_list.append(contact)

   f.close()

def store_python_pickle(python_list):
   f = open("PythonS/python_db.data", "wb")   #바이너리 파일로 불러올 때는 확장자도 바꿔줘야 한다.
   import pickle #굳이 맨 위에 정의하지 않아도 된다. 
   pickle.dump(python_list, f)    #꺼내서 하나하나씩 저장할 필요가 없다. 리스트 통째로 저장한다.
   f.close()

def load_python_pickle():  #파라미터가 굳이 필요없다. call by value처럼 동작하기 때문에
   f = open("PythonS/python_db.data", "rb")
   import pickle
   python_list = pickle.load(f)   # 통째로 받아와서 다시 저장한다. .을 안 찍고 =으로 받기 때문에 이전 게 사라지고 새로운 객체가 들어온다.
#   객체 형태로 모두 들어간다. 리스트형태로 모두 들어간다. 
   f.close()
   return python_list #왜 굳이 return을 해야될까? 객체니까 contact_list의 주소값을 전달해준다. 

def load_jsp_fwrite(jsp_list):
   f = open("PythonS/jsp_db.txt", "rt")
#   readlines()는 모든 행을 저장한다. 5명이면 20줄이 저장된다. 
   lines = f.readlines()   #lines에는 리스트가 들어간다. 총 4개. 개행까지 포함한 문자열로.
   num = len(lines) / 4    # 4 / 4인데 나누면 float연산이 된다. 1.0이 나와서 num에는 1.0이 들어간다. 
   num = int(num)          # 1.0을 정수로 고쳐주기 위해서 int를 써준다.
   
   #주소록의 개수만큼 돌아라. 
   for i in range(num):
       error = lines[4*i].rstrip('\n')  #rstrip은 맨 오른쪽의 문자를 없앤다는 뜻. 즉, 개행을 없앤다. \n을 지워주기 위해서.
       #왜? 데이터 안에 개행이 있으면 안 되니까. 나중에 출력할 때 줄바꿈이 더 되기도 하고. 
       # 만약에 중간에 개행이 있다면 replace를 써줘야 한다. 
       read = lines[4*i+1].rstrip('\n')
       answer = lines[4*i+2].rstrip('\n')
       contact = Contact(error, read, answer)
       jsp_list.append(contact)
   f.close()

def store_jsp_print(jsp_list):
   f = open("PythonS/jsp_db.txt", "wt")
   for contact in jsp_list:
#       print는 가변인자라서 여러 변수를 써도 된다. contact를 하나씩 빼온다. 한 행 안의 파일이 ,로 구분되어 있는 파일(cvs), sep의 default는 ' ' end의 디폴트는
#       'n'이고 파일에 저장해야 하니까 file=f.
       print(contact.error, contact.read, contact.answer, file=f, sep=',')
   f.close()

def load_jsp_print(jsp_list):   #얘네들은 call by reference이다. contact_list.append이니까. 이 라인에 있는 파라미터(contact_list)에 가서 넣는 것이다.
   f = open("PythonS/jsp_db.txt", "rt")
   lines = f.readlines() #readlines는 모든 행을 다 읽는데 리스트로 들어가서 ['ㅁ,ㄴ,ㅇ,ㄹ', 'ㅁ,ㄴ,ㅇ,ㄹ',]이런 식...''안에는 문자열이다. 
   for line in lines:  #lines 리스트 안에 있는 만큼 line을 실행. line도 리스트가 된다. 
       data = line.split(',')  #구분 기호를 집어넣는다. split은 기본이 공백이다. Line이 리스트니까 공백을 구분 단위로 한다. 
       contact = Contact(data[0], data[1], data[2])   #0번째는 이름, 1번째는 전화번호... 칼럼이 늘어나면 그대로 다시 넣어줘야 한다. 
       jsp_list.append(contact)

   f.close()

def store_jsp_pickle(jsp_list):
   f = open("PythonS/jsp_db.data", "wb")   #바이너리 파일로 불러올 때는 확장자도 바꿔줘야 한다.
   import pickle #굳이 맨 위에 정의하지 않아도 된다. 
   pickle.dump(jsp_list, f)    #꺼내서 하나하나씩 저장할 필요가 없다. 리스트 통째로 저장한다.
   f.close()

def load_jsp_pickle():  #파라미터가 굳이 필요없다. call by value처럼 동작하기 때문에
   f = open("PythonS/jsp_db.data", "rb")
   import pickle
   jsp_list = pickle.load(f)   # 통째로 받아와서 다시 저장한다. .을 안 찍고 =으로 받기 때문에 이전 게 사라지고 새로운 객체가 들어온다.
#   객체 형태로 모두 들어간다. 리스트형태로 모두 들어간다. 
   f.close()
   return jsp_list  # 왜 굳이 return을 해야될까? 객체니까 contact_list의 주소값을 전달해준다.
   
def run():
   java_list = []   #contact_list를 리스트로 지정해준다. 
   python_list = []
   jsp_list = []
   print(java_list)
   print(python_list)
   print(jsp_list)
   try:
      java_list = load_java_pickle()
      python_list = load_python_pickle()
      jsp_list = load_jsp_pickle()
   except OSError as e:
      print(e)
   while 1:    #무한 루프로 돌게 한다. 사용자가 입력을 안 한다고 할 때까지 입력을 받아야 하니까.
      menu = print_menu()    #메뉴를 화면에 띄워야 하니까. #print_menu에서 리턴된 정수 menu를 다시 menu변수에 넣는다.
      menu4 = print_menu4()
      if menu == 1:   #java 에러
         print_java(java_list)
      elif menu == 2:     #python 에러
         print_python(python_list)
      elif menu == 3:     #jsp 에러
         print_jsp(jsp_list)
      elif menu == 4:     #에러 추가
         if menu4 == 1:
            contact = set_contact()     
            java_list.append(contact)    #추가한다.
         elif menu4 == 2:
            contact = set_contact()     
            python_list.append(contact)    #추가한다.
         elif menu4 == 3:
            contact = set_contact()     
            jsp_list.append(contact)    #추가한다.
         else:
            break
      elif menu == 5:     #에러 저장
         store_java_pickle(java_list)
         store_python_pickle(python_list)
         store_jsp_pickle(jsp_list)
      elif menu == 6:     #종료
         break
      else:
         break
   
   
if __name__ == "__main__":  #다른 모듈에 의해 import될 때 여기 있는 main이 먼저 호출되면 안 되니까. 
                           #스스로 실행될 때만 이 main이 실행되게 하려고. 
   run()
