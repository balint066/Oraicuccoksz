import math
class Teglalap:
    a = 0
    b = 0

    def ter(self):
        return self.a*self.b

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def ker(self):
        return 2*(self.a+self.b)

    def atlo(self):
        return  math.sqrt(self.a**2+self.b**2)

    def atlofele(self):
        return self.atlo()/2

    def korekor(self):
        return Kor(self.atlofele())

    def tegkort(self):
        return self.atlofele()**2*math.pi

    def tegkork(self):
        return self.atlofele()*2*math.pi

    def kiir(self):
        return print("A téglalap Kerülete:", self.ker(), " ", "Területe:", self.ter(), "Átló hossza:",self.atlo(),
                     "köréírható körének hossza:", self.atlofele(), "köréírható körének kerülete:", self.korekor().kork(),
                     "köréírható körének területe:", self.korekor().kort())

class Kor:
    r = 0
    def __init__(self, r=0,):
        self.r = r

    def kork(self):
        return 2*self.r*math.pi

    def kort(self):
        return self.r**2*math.pi
    def kkir(self):
        return print("a kor kerülete", self.kork(), "területe", self.kort())
