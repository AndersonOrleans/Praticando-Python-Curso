cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adiacente = float(input('Comprimento do cateto adiacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adiacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
