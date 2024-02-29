import math

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

delta = b*b - 4*a*c

x1 = (-b + math.sqrt(delta))/2
x2 = (-b - math.sqrt(delta))/2

print(x1, x2)