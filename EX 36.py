numero = int(input('Digite um número: '))
print('''Escolha umas das bases para conversão: 
[1] Converter para BINÁRIO.
[2] Converter para OCTAL.
[3] Converter para HEXADECIMAL.''')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print(f'O número: {numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'O número: {numero} convertido para OCTAL é igual a {oct(numero[2:])}.')
elif opcao == 3:
    print(f'O número: {numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}.')
else:
    print('Opção inválida. Tente novamente!')
