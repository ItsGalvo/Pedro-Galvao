idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade (brasileira ou estrangeira): ")

if idade >= 18 and nacionalidade.lower() == 'brasileira':
    print("Você pode votar.")
else:
    print("Você não pode votar.")