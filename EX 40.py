print('Bem vindo (a) a compretição de natação de Florianópolis - SC - 2023.')
print()
print('Preencha sua ficha: ')
print()
ano_atual = 2023
nome = str(input('Digite seu nome: '))
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print(f'Olá, {nome}, sua idade é: {idade} anos, sua categoria na competição é: MIRIM.')
elif idade <= 14:
    print(f'Olá, {nome}, sua idade é: {idade} anos, sua categoria na competição é: INFANTIL.')
elif idade <= 19:
    print(f'Olá, {nome}, sua idade é: {idade} anos, sua categoria na competição é: JUNIOR.')
elif idade <= 25:
    print(f'Olá, {nome}, sua idade é: {idade} anos, sua categoria na competição é: SÊNIOR.')
else:
    print(f'Olá, {nome}, sua idade é: {idade} anos, sua categoria na competição é: MASTER.')
    