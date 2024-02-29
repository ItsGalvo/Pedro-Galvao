num_alunos = int(input("Quantos alunos deseja cadastrar? "))
alunos = {}
for i in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

alunos_aprovados = {nome: nota for nome, nota in alunos.items() if nota >= 7}

print("\nAlunos aprovados:")
print(alunos_aprovados)
