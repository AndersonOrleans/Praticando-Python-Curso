km = float(input('Digite a quantidade de km percorrido: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
pagar = (km * 0.15) + (dias * 60)
print(f'Você alugou o carro por: {dias} dias, e percorreu {km} km. O valor total do aluguel: R$ {pagar:.2f} reais.')

