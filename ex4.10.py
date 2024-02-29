frase = input("Digite uma frase: ")

artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']

frase_sem_artigos = ' '.join([palavra for palavra in frase.split() if palavra.lower() not in artigos])

print("\nFrase sem artigos:")
print(frase_sem_artigos)
