numero = int(input("Digite um número para verificar se é perfeito: "))

soma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if soma_divisores == numero:
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")