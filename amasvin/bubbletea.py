from drink import Drink

class Bubbletea(Drink) :
    def __init__(self, name, price) :
        super().__init__(name, price)
        self.pearl = 0 #0:타피오카, 1:코코, 2:젤리, 3:알로에

    def set_pearl(self) :
        self.pearl = input("펄을 선택하세요(0:타피오카, 1:코코, 2:젤리, 3:알로에):")
        if self.pearl == "" :
            self.pearl = 0 #0:타피오카, 1:코코, 2:젤리, 3:알로에
        else :
            self.pearl = int(self.pearl)

    def __str__(self) :
        return super().__str__() + "\t펄 : " + self._pearls[self.pearl]

    def order(self) :
        # self.set_cup
        # self.set_ice
        # self.set_sugar (이 세줄의 아이들은 부모의 것을 불러오도록 한다.)
        super().order()
        self.set_pearl
