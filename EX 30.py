valor_1 = 0.50
valor_2 = 0.45
distancia = float(input('Digite a distância da sua viagem em km: '))
if distancia <= 200:
    valor_total = distancia * valor_1
    print(f'O valor total para viagens até 200 km é R$ 0,50 reais. Você fez uma viagem de {distancia} km, o valor total: R$ {valor_total:.2f} reais.')
elif distancia > 200:
    valor_total = distancia * valor_2
    print(f'O valor total para viagens mais longas é R$ 0,45 reais. Você fez uma viagem de {distancia} km, o valor total: R$ {valor_total:.2f} reais.')
