def calcular_media(lista1, lista2):
    if len(lista1) != len(lista2):
        return "As listas não têm o mesmo tamanho"
    
    medias = [(lista1[i] + lista2[i]) / 2 for i in range(len(lista1))]
    return medias

lista1 = [float(x) for x in input("Digite os elementos da primeira lista separados por espaço: ").split()]
lista2 = [float(x) for x in input("Digite os elementos da segunda lista separados por espaço: ").split()]

resultado = calcular_media(lista1, lista2)

print("Média dos elementos correspondentes:", resultado)
