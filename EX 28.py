multa = 7
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você ultrapassou a velocidade permitida de 80km/h!')
    valor_da_multa = (velocidade - 80) * 7
    print(f'O valor total da multa: R$ {valor_da_multa:.2f} reais. ')
    print('Tenha um bom dia! Dirija com cuidado, use cinto de segurança!')
else:
    print(f'Você não foi multado, seu carro estava na velocidade: {velocidade}km/h, continue dirigindo com cuidado. Use cinto de segurança!')
