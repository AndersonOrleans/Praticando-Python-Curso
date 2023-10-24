reta_1 = float(input('Digite o primeiro segmento: '))
reta_2 = float(input('Digite o segundo segmento: '))
reta_3 = float(input('Dgite o terceiro segmento: '))
if reta_1 == reta_2 == reta_3 == reta_1:
    print('Todos os lados são iguais: Triângulo EQUILÁTERO.')
elif reta_1 != reta_2 != reta_3 != reta_1:
    print('Todos os lados são diferentes: Triângulo ESCALENO.')
else:
    print('Dois lados são iguais: Triângulo ISÓSCELES.')
