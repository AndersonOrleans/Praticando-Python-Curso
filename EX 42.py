nome = str(input('Digite seu nome: '))
peso = float(input(f'Olá {nome}, qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura ** 2)
print(f'{nome}, seu IMC é {imc:.1f}.')
if imc <= 18.5:
    print(f'Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em obsidade!')
elif imc >= 40:
    print('Você está em obsidade mórbida, cuidado!')
