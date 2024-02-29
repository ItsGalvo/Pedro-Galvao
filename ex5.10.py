palavras = input("Digite uma lista de palavras separadas por espaço: ").split()

comprimentos = [len(palavra) for palavra in palavras]

print("Comprimentos de cada palavra:", comprimentos)
