reta_1 = float(input('Digite o primeiro segmento: '))
reta_2 = float(input('Digite o segundo segmento: '))
reta_3 = float(input('Dgite o terceiro segmento: '))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os segmento acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmento acima NÃO PODEM FORMAR UM TRIÂNGULO!')
