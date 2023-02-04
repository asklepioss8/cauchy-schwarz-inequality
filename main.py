import engine
import matplotlib.pyplot as plt


class Main(engine.Schwarz):
    x = []
    y1 = []
    y2 = []


    @classmethod
    def grapher(cls):
        plt.plot(cls.x, cls.y1, "y")
        plt.plot(cls.x, cls.y2, "b")

    def main(self):

        for i in range(self.arr_len):
            self.count = i
            Main.x.append(i)
            Main.y1.append(self.left_handside())
            Main.y2.append(self.right_hand_side())


test = Main(1000)
test.rand_main()
test.main()
test.grapher()




plt.show()













