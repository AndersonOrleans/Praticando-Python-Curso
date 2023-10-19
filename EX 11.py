largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de: {largura} Largura por {altura} Altura e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta} litros de tinta.')
