salario = float(input('Qual é o valor do salário do funcionário: '))
if salario <= 1250:
    novo_salario = salario + (salario * 15 /100)
else:
    novo_salario = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {novo_salario:.2f} reais.')
