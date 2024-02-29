nome = input("Digite o nome da pessoa: ")
salario = float(input("Digite o salário da pessoa: "))
imposto = float(input("Digite o valor do imposto sobre o salário: "))

salario_liquido = salario - imposto

print("O salário líquido de", nome, "é:", salario_liquido)