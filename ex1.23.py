distancia = float(input("Digite a distância percorrida pelo objeto (em metros): "))
tempo = float(input("Digite o tempo gasto pelo objeto (em segundos): "))
aceleracao = float(input("Digite a aceleração do objeto (em metros por segundo ao quadrado): "))

velocidade_final = (2 * distancia / tempo - aceleracao * tempo) / 2

velocidade_inicial = velocidade_final - aceleracao * tempo

print("A velocidade inicial do objeto é:", velocidade_inicial, "metros por segundo")
print("A velocidade final do objeto é:", velocidade_final, "metros por segundo")