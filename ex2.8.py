entrada = input("Digite uma string para verificar se é um número real: ")

eh_numero_real = True

caracteres_validos = "0123456789."

if entrada == "":
    eh_numero_real = False

if entrada[0] == '+' or entrada[0] == '-':
    entrada = entrada[1:]  

if entrada.count('.') > 1:
    eh_numero_real = False

for char in entrada:
    if char not in caracteres_validos:
        eh_numero_real = False
        break

if eh_numero_real:
    print("É um número real.")
else:
    print("Não é um número real.")