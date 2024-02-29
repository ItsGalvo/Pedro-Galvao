genero = input("Digite seu gênero (M para masculino, F para feminino): ")

if genero.upper() == 'M':
    print("Gênero masculino")
elif genero.upper() == 'F':
    print("Gênero feminino")
else:
    print("Gênero não reconhecido")
