from coffee import Coffee
from bubbletea import Bubbletea

class Order :
    _drinks = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]
    def __init__(self) :
        self.order_menu = []

    def show_menu(self) :
        print("0:아메리카노1800원, 1:딸기요거트3500원")

    def order_drink(self) :
        #반복↓
        while True:
            #1. show menu
            self.show_menu()
            #2. 주문받자, 음료선택하자
            order = input("무엇을 고르시겠습니까? ")
            if order == "":
                break
            drink = Order._drinks[int(order)]
            #3. 음료 옵션선택하자
            drink.order()
            self.order_menu.append(drink)
        #반복↑
        #4. 주문한 음료 내용 보여주자
        for d in self.order_menu:
            print(d)
        #5. 합계 금액 보여주자
        # self.sum_price()
        print("총 금액 : "+ str(self.sum_price()) + "원")

    def sum_price(self):
        sum = 0
        for d in self.order_menu:
            sum += d.price

        return sum

아메리카노 = Coffee("아메리카노", 1800)
아메리카노.set_cup()
아메리카노.set_ice()
아메리카노.set_sugar()
print(아메리카노)

딸기요거트 = Bubbletea("딸기요거트", 3500)
딸기요거트.set_cup()
딸기요거트.set_ice()
딸기요거트.set_sugar()
딸기요거트.set_pearl()
print(딸기요거트)
