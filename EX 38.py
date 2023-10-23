from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano do seu nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem hoje {idade} anos em {atual}.')
if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
