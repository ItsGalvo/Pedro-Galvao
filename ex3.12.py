soma = 0

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        soma += num

print("A soma dos números primos de 1 a 100 é:", soma)