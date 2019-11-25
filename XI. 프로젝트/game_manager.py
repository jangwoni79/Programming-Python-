from tictactoe import TicTacToe
import tkinter
from tkinter import messagebox
import math


class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주자
        print(self.ttt)
        while True:
            #row, col 입력받자
            row = int(input("row : "))
            col = int(input("col :"))
            self.ttt.set(row, col)
            print(self.ttt)

            #check_winner 면 끝내자
            if self.ttt.check_winner() == "O":
                print("O win!!!")
                break
            elif self.ttt.check_winner() == "X":
                print("X win!!!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

class GameManager_GUI:
    def __init__(self):
        self.ttt = TicTacToe()
        CANVAS_SIZE = 300
        self.TITLE_SIZE = CANVAS_SIZE / 3

        self.root = tkinter.Tk()
        self.root.title("틱텍토")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE)) #"300 x 300"
        self.root.resizable(width=False, height=False) #창크기 변경 못함
        self.canvas = tkinter.Canvas(self.root, bg = "white", width = CANVAS_SIZE, height = CANVAS_SIZE)
        self.canvas.pack()

        self.imges = dict()
        self.imges["O"] = tkinter.PhotoImage(file = "img/O.gif")
        self.imges["X"] = tkinter.PhotoImage(file="img/X.gif")

        self.canvas.bind("<Button-1>", self.Click_handler)

    def Click_handler(self, event):
        row = int(event.y//self.TITLE_SIZE)
        col = int(event.x//self.TITLE_SIZE)
        print(row, col)
        self.ttt.set(row, col)
        self.draw_board()
        # print(self.ttt)
        #draw_board()
        #check__winner()
        if self.ttt.check_winner == "O":
            messagebox.showinfo("게임 오버", "O win!!!")
            self.root.quit()
        elif self.ttt.check_winner == "X":
            messagebox.showinfo("게임 오버", "X win!!!")
            self.root.quit()
        elif self.ttt.check_winner == "d":
            messagebox.showinfo("게임 오버", "무승부")
            self.root.quit()

    def draw_board(self):
        #clear
        self.canvas.delete("all")

        x = 0
        y = 0
        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "O":
                self.canvas.create_image(x, y, anchor = "nw", image = self.images["O"])
            elif v == "X":
                self.canvas.create_image(x, y, anchor = "nw", image = self.images["X"])
            x += self.TITLE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TITLE_SIZE

    def play(self):
        self.root.mainloop()

if __name__ == '__main__':
    gm = GameManager_GUI()
    gm.play()

