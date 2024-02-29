numeros = [float(x) for x in input("Digite a lista de números separados por espaço: ").split()]

numero_referencia = float(input("Digite o número de referência: "))

posicao = None

for i, numero in enumerate(numeros):
    if numero > numero_referencia:
        posicao = i
        break

if posicao is not None:
    print(f"A posição do primeiro elemento maior que {numero_referencia} é: {posicao}")
else:
    print(f"Nenhum elemento na lista é maior que {numero_referencia}")
