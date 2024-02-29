frase = input("Digite uma frase: ")

palavras = frase.split()

contagem_o = 0
contagem_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        contagem_o += 1
    elif palavra.endswith('a'):
        contagem_a += 1

print("Número de palavras terminadas com 'o':", contagem_o)
print("Número de palavras terminadas com 'a':", contagem_a)
