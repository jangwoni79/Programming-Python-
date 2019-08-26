class Search:
    def __init__(self, error, read, answer):  # 생성자 함수
        self.error = error
        self.read = read
        self.answer = answer

    def print_info(self):  # 정보 출력 함수
        print("")
        print("Error : ", self.error)
        print("Read : ", self.read)
        print("Answer : ", self.answer)


def set_search():
    print("")
    error = input("Error : ")
    read = input("Read : ")
    answer = input("Answer : ")
    search = Search(error, read, answer)  # 입력한 변수 초기화
    return search


def print_menu():  # 메뉴 출력
    print("")
    print("!!프로그래밍 언어를 선택해 주세요!!")
    print("▶ 보기 ◀")
    print("1. JAVA")
    print("2. Python")
    print("3. JSP")
    print("4. error 추가")
    print("5. error 삭제")
    print("6. error 저장")
    print("7. 종료")
    print("")
    menu = input("메뉴 선택 : ")
    return int(menu)  # 입력 시 문자열로 들어가기 때문에 int로 바꿔줌


def print_menu4():  # 메뉴4번의 추가 메뉴
    print("")
    print("!!추가하고 싶은 프로그래밍 언어를 선택해 주세요!!")
    print("▶ 보기 ◀")
    print("1. JAVA")
    print("2. Python")
    print("3. JSP")
    print("4. 종료")
    menu4 = input("메뉴 선택 : ")
    return int(menu4)

def print_menu5():
    print("")
    print("!!삭제하고 싶은 에러를 선택해 주세요!!")
    print("▶ 보기 ◀")
    print("1. JAVA")
    print("2. Python")
    print("3. JSP")
    print("4. 종료")
    menu5 = input("메뉴 선택 : ")
    return int(menu5)

def print_java(java_list):  # java에러 정보 출력
    for search in java_list:
        search.print_info()  # 정보 출력


def print_python(python_list):  # python에러 정보 출력
    for search in python_list:
        search.print_info()  # 정보 출력


def print_jsp(jsp_list):  # jsp에러 정보 출력
    for search in jsp_list:
        search.print_info()  # 정보 출력


def store_java(java_list):
    f = open("PythonS/java_db.txt", "wt")  # txt파일을 열고 써야하니까 wt모드 사용
    for search in java_list:
        f.write(search.error + '\n')  # 입력한 정보를 각자 넣어줌
        f.write(search.read + '\n')
        f.write(search.answer + '\n')
    f.close()


def load_java(java_list):
    f = open("PythonS/java_db.txt", "rt")
    lines = f.readlines()  # 입력한 수 만큼 *3해서 저장됨
    num = len(lines) / 3  # lines에는 리스트가 문자열로 3개(error, read, answer)가 들어간다
    num = int(num)  # 1.0을 정수로 고쳐주기 위함

    for i in range(num):  # 에러 정보록의 개수만큼 돌림
        # rstrip은 맨 오른쪽의 문자를 없앤다는 뜻 → 즉, \n을 지워줌(데이터 안에는 \n이 있으면 안됨)
        error = lines[3*i].rstrip('\n')
        read = lines[3*i+1].rstrip('\n')
        answer = lines[3*i+2].rstrip('\n')
        search = Search(error, read, answer)
        java_list.append(search)
    f.close()


def store_python(python_list):
    f = open("PythonS/python_db.txt", "wt")  # txt파일을 열고 써야하니까 wt모드 사용
    for search in python_list:
        f.write(search.error + '\n')  # 입력한 정보를 각자 넣어줌
        f.write(search.read + '\n')
        f.write(search.answer + '\n')
    f.close()


def load_python(python_list):
    f = open("PythonS/python_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 3
    num = int(num)

    for i in range(num):
        error = lines[3*i].rstrip('\n')
        read = lines[3*i+1].rstrip('\n')
        answer = lines[3*i+2].rstrip('\n')
        search = Search(error, read, answer)
        python_list.append(search)
    f.close()


def store_jsp(jsp_list):
    f = open("PythonS/jsp_db.txt", "wt")  # txt파일을 열고 써야하니까 wt모드 사용
    for search in jsp_list:
        f.write(search.error + '\n')  # 입력한 정보를 각자 넣어줌
        f.write(search.read + '\n')
        f.write(search.answer + '\n')
    f.close()


def load_jsp(jsp_list):
    f = open("PythonS/jsp_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 3  # 3/3인데 나누면 float연산이 된다. 1.0이 나와서 num에는 1.0이 들어간다
    num = int(num)  # 1.0을 고쳐주기 위함

    for i in range(num):
        error = lines[3*i].rstrip('\n')
        read = lines[3*i+1].rstrip('\n')
        answer = lines[3*i+2].rstrip('\n')
        search = Search(error, read, answer)
        jsp_list.append(search)
    f.close()

def delete_java(java_list, error): #java에러 삭제
    for i, contact in enumerate(java_list):
        if contact.error == error:
            del java_list[i]

def delete_python(python_list, error): #python에러 삭제
    for i, contact in enumerate(python_list):
        if contact.error == error:
            del python_list[i]

def delete_jsp(jsp_list, error): #jsp에러 삭제
    for i, contact in enumerate(jsp_list):
        if contact.error == error:
            del jsp_list[i]

def run():
    java_list = [] #리스트 만들기
    python_list = []
    jsp_list = []
    load_java(java_list)
    load_python(python_list)
    load_jsp(jsp_list)

    print("▶ Error Catch ◀")
    print("설명 - 원하시는 에러를 검색할 수 있습니다.")
    
    while 1: 
        menu = print_menu()
        if menu == 1: #menu1 - java에러 출력
            print_java(java_list)
        elif menu == 2: #menu2 - python에러 출력
            print_python(python_list)
        elif menu == 3: #menu3 - jsp에러 출력
            print_jsp(jsp_list)
        elif menu == 4:
            menu4 = print_menu4()
            if menu4 == 1:
                search = set_search()
                java_list.append(search)
                store_java(java_list)
            elif menu4 == 2:
                search = set_search()
                python_list.append(search)
                store_python(python_list)
            elif menu4 == 3:
                search = set_search()
                jsp_list.append(search)
                store_jsp(jsp_list)
        elif menu == 5:
            menu5 = print_menu5()
            if menu5 == 1:
                print_java(java_list)
                print("")
                error = input("Error : ")
                delete_java(java_list, error) 
                print("해당 에러가 삭제되었습니다.")
            elif menu5 == 2:
                print_python(python_list)
                print("")
                error = input("Error : ")
                delete_python(python_list, error)
                print("해당 에러가 삭제되었습니다.")
            elif menu5 == 3:
                print_jsp(jsp_list)
                print("")
                error = input("Error : ")
                delete_jsp(jsp_list, error)
                print("해당 에러가 삭제되었습니다.")
            else :
                break
        elif menu == 6:
            print("")
            a = str(input("저장하시겠습니까? (y/n) : "))
            if a == 'y' and a == 'Y':
                print("수정된 사항이 저장되었습니다.")
                store_java(java_list)
                store_python(python_list)
                store_jsp(jsp_list)
            elif a == 'n' and a == 'N':
                continue
        elif menu == 7:
                store_java(java_list)
                store_python(python_list)
                store_jsp(jsp_list)
                break
if __name__ == "__main__":
    run()
