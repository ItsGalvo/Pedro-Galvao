numero = int(input("Digite um número para verificar se é primo: "))

is_primo = True
if numero <= 1:
    is_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break

if is_primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")