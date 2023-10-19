nome = str(input('Qual é seu nome completo?: ')).strip()
print(f'Seu nome tem Orleans? {("orleans", "ORLEANS" in nome.lower().upper())}')
