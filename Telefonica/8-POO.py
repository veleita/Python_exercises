from math import gcd, lcm


from math import lcm, gcd

class Fraccion():
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __str__(self) -> str:
        return str(self.dividendo) + "/" + str(self.divisor)
    
    def sumar(self, other):
        multiplier = lcm(self.divisor, other.divisor)
        new_dividend = int(self.dividendo * (multiplier/self.divisor) + other.dividendo * (multiplier/other.divisor))
        return Fraccion(new_dividend, multiplier)
    
    def multiplicar(self, other):
        return Fraccion(self.dividendo * other.dividendo, self.divisor * other.divisor)
    
    def simplificar(self):
        reductor = gcd(self.divisor, self.dividendo)
        return Fraccion(self.dividendo // reductor, self.divisor // reductor)

a = Fraccion(2, 6)
b = Fraccion(1, 2)
sum = a.sumar(b)
print(a.__str__(), " + ", b.__str__(), " = ", sum.__str__())
mult = a.multiplicar(b)
print(a.__str__(), " * ", b.__str__(), " = ", mult.__str__())
sim = mult.simplificar()
print(mult.__str__(), " = ", sim.__str__())