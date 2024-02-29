frase = input("Digite uma frase: ")

palavras = frase.split()

palavras_limpas = [palavra.strip() for palavra in palavras]

frase_nova = ' '.join(palavras_limpas)

print("Frase com espaços em branco removidos:")
print(frase_nova)
