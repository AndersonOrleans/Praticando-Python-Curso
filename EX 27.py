from random import randint
computador = randint(0,5)
nome_jogador = str(input('Olá, seja bem vido(a) ao jogo! Digite o seu nome: '))
print('Computador diz: Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input(f'Jogador {nome_jogador} diz: Eu pensei no número: '))
if jogador == computador:
    print(f'Parabéns {nome_jogador}! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}! Computador venceu!')
