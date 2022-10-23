numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while numero > 20 or numero < 0:
    print('Tente novamente. ', end='')
    numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[numero]}')
