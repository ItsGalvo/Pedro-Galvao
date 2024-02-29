num_alunos = int(input("Quantos alunos deseja cadastrar? "))
alunos = {}
for i in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

alunos_arredondados = {nome: round(nota) for nome, nota in alunos.items()}

print("\nNotas arredondadas dos alunos:")
print(alunos_arredondados)
