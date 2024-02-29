frase = input("Digite uma frase: ")

palavras_modificadas = [palavra.replace('a', 'o') for palavra in frase.split() if 'a' in palavra]

print(palavras_modificadas)
