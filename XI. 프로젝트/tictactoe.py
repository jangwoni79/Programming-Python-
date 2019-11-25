class TicTacToe:
    def __init__(self):
        self.borad = [".", ".", ".", \
                      ".", ".", ".", \
                      ".", ".", "."]
        self.current_turn = "X"

    def set(self, row, col):
        if self.get(row, col) == ".":
            if self.current_turn == "O":
                self.current_turn = "X"
            else:
                self.current_turn = "O"
                self.borad[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.borad[(row * 3) + col]

    def check_winner(self, row, col):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check:
                # -
                return check
            elif self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
                # |
                return check
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            # \
            return check
        if self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
            # /
            return check

        if not "." in self.borad:
            return "d"  # 비김

    def __str__(self):
        s = ""
        for i, v in enumerate(self.borad):
            s += v
            if i % 3 == 2:
                s += "\n"

        return None