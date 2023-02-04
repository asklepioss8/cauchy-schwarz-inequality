import randomx


class Schwarz(randomx.Randomx):

    def __init__(self, arr_len):
        super().__init__(arr_len)
        self.count = None


    def right_hand_side(self):
        reg3 = 0
        reg4 = 0
        for i in range(self.count):
            reg3 += (self.arr1[i]**2)
            reg4 += (self.arr2[i] ** 2)
        return (reg3 * reg4) ** (1/2)

    def left_handside(self):
        reg2 = 0
        for i in range(self.count):
            reg2 += self.arr1[i] * self.arr2[i]
        return reg2


    def engine(self):
        pass














