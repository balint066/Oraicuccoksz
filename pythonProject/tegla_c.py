class Teglalap:

    def ter(self):
        return self.a * self.b

    def ker(self):
        return 2 * (self.a + self.b)

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def kiir(self):
        print("a téglalap területe: ", self.ter(), ",a kerülete: ", self.ker())
