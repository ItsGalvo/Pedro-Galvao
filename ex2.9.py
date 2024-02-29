data = input("Digite uma data no formato mm/dd/aaaa: ")

eh_data_valida = True

if len(data) != 10:
    eh_data_valida = False
else:
    partes = data.split('/')

    if len(partes) != 3:
        eh_data_valida = False
    else:
        mes, dia, ano = partes
        
        if not (mes.isdigit() and dia.isdigit() and ano.isdigit()):
            eh_data_valida = False
        else:
            mes = int(mes)
            if not (1 <= mes <= 12):
                eh_data_valida = False
            else:
                dia = int(dia)
                if not (1 <= dia <= 31):
                    eh_data_valida = False

if eh_data_valida:
    print("A entrada é uma data válida")
else:
    print("A entrada não é uma data válida")