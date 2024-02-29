import cmath

print("Insira o primeiro número complexo:")
real1 = float(input("Parte real: "))
imag1 = float(input("Parte imaginária: "))
numero1 = complex(real1, imag1)

print("\nInsira o segundo número complexo:")
real2 = float(input("Parte real: "))
imag2 = float(input("Parte imaginária: "))
numero2 = complex(real2, imag2)

soma = numero1 + numero2
produto = numero1 * numero2

print("\nA soma dos números complexos é:", soma)
print("O produto dos números complexos é:", produto)
