numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("O maior número na lista é:", maior)
print("O menor número na lista é:", menor)
