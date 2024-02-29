numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_ordenados = sorted(set(numeros))
segundo_menor = numeros_ordenados[1]
segundo_maior = numeros_ordenados[-2]

print("O segundo menor número na lista é:", segundo_menor)
print("O segundo maior número na lista é:", segundo_maior)