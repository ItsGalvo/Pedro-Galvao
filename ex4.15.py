frase = input("Digite uma frase: ")

palavras = frase.split()

ocorrencias = {}
for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

print("Número de ocorrências de cada palavra na frase:")
for palavra, quantidade in ocorrencias.items():
    print(f"A palavra '{palavra}' aparece {quantidade} vezes.")
