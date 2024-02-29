import math

numero = float(input("Digite um número (em graus): "))

numero_radianos = math.radians(numero)

seno = math.sin(numero_radianos)
cosseno = math.cos(numero_radianos)
tangente = math.tan(numero_radianos)

# Imprime os resultados
print(f"O seno de {numero} é: {seno}")
print(f"O cosseno de {numero} é: {cosseno}")
print(f"A tangente de {numero} é: {tangente}")
