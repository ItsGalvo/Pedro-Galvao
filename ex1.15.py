distancia = float(input("Digite a distância: "))
velocidade_inicial = float(input("Digite a velocidade inicial: "))

aceleracao_gravidade = 9.81

tempo_queda = (0-velocidade_inicial)/-aceleracao_gravidade

a = 0.5 * -aceleracao_gravidade
b = velocidade_inicial
c = -distancia

tempo_queda = (-b-(b**2-4*a*c)**0.5)/(2*a)

print("O tempo para atingir o solo é de", tempo_queda, "segundos.")