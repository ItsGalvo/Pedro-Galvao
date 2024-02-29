numero = int(input("Digite um número para ver sua tabuada: "))

print("Tabuada do", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)