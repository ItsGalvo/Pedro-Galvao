teste = input("Digite algo: ")
numeros = "0123456789"
inteiro = True
for caractere in teste:
    if caractere not in numeros:
        inteiro = False
        break
if inteiro:
    print("O número é inteiro")
else:
    print("Não é um número")