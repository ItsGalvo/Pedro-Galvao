frase = input("Digite uma frase: ")
palavra_presente = input("Digite uma palavra presente na frase: ")
palavra_ausente = input("Digite uma palavra ausente na frase: ")

frase_modificada = frase.replace(palavra_presente, palavra_ausente)

print("\nFrase modificada:")
print(frase_modificada)
