casa = float(input('Qual o valor da casa?: R$ '))
salario = float(input('Qual é o valor do salário?: R$ '))
anos = int(input('Você deseja pagar a casa em quantos anos?: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar um casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}.')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')