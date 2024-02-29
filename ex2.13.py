idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (homem ou mulher): ")

if (genero.lower() == 'mulher' and idade >= 60) or (genero.lower() == 'homem' and idade >= 65):
    print("Você é elegível para aposentadoria.")
else:
    print("Você ainda não é elegível para aposentadoria.")
