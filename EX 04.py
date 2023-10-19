digite = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {digite}', type(digite))
print('Só tem espaço?', digite.isspace())
print('É um número?', digite.isnumeric())
print('É alfabético?', digite.isalpha())
print('É alfanúmerico?', digite.isalpha())
print('Está em maiúsculas?', digite.isupper())
print('Está em minúsculas?', digite.islower())
print('Está capitalizada?', digite.istitle())


