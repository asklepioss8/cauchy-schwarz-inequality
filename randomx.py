import random


class Randomx:

    def __init__(self, arr_len):
        self.arr_len = arr_len
        self.arr1 = []
        self.arr2 = []

    def rand_array(self):
        reg1 = []
        for i in range(self.arr_len):
            reg1.append(random.randint(1, 100))
        return reg1

    def rand_main(self):
        self.arr1 = Randomx.rand_array(self)
        self.arr2 = Randomx.rand_array(self)



