valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros (em %): ")) / 100
anos = int(input("Digite o número de anos: "))
valor_final = valor_inicial * (1 + taxa_juros) ** anos
print("O valor final do investimento após", anos, "anos será de:", valor_final)