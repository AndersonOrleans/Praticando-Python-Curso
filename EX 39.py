nome = str(input('Digite o nome do aluno: '))
print(f'Digite as notas do aluno: {nome}.')
print()
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print(f'A média do aluno: {nome} foi: {media}. Reprovado!')
elif media >= 5 and media < 7:
    print(f'A média do aluno: {nome} foi: {media}. Recuperação!')
elif media >= 7:
    print(f'A média do aluno: {nome} foi {media}. Aprovado.')

