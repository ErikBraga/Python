from random import randint
n_computador = randint(0, 10)
n_usuario = 11
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while n_usuario != n_computador:
    n_usuario = int(input('Qual é seu palpite? '))
    tentativas += 1  # contador de tentativas
    if n_computador < n_usuario:
        print('Menos... Tente outra vez.')
    elif n_computador > n_usuario:
        print('Mais... Tente outra vez.')
print(f'Acertou com {tentativas} tentativas. Parabéns!')
