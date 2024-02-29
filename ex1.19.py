velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
velocidade_final = float(input("Digite a velocidade final (em m/s): "))
tempo = float(input("Digite o tempo de transição (em segundos): "))

aceleracao = (velocidade_final - velocidade_inicial) / tempo

print("A aceleração é:", aceleracao, "m/s^2")