nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')

