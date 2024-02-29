nomes = input("Digite os nomes dos alunos separados por espaço: ").split()
notas = [float(x) for x in input("Digite as notas dos alunos separadas por espaço: ").split()]

alunos_notas = list(zip(nomes, notas))

alunos_notas_ordenados = sorted(alunos_notas, key=lambda x: x[1], reverse=True)

print("Lista de alunos e notas em ordem decrescente de nota:")
for aluno, nota in alunos_notas_ordenados:
    print(aluno, "-", nota)
