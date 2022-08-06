from random import randint
from time import sleep

jogada = randint(0, 5)  # gera um número aleatório entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
tentativa = int(input('Em que número eu pensei? '))  # palpite do usuário
print('PROCESSANDO...')
sleep(0.5)
if tentativa > 5:  # bloqueia números maiores que 5
    print('Número inválido.')
if tentativa < 0:  # bloqueia números menores que 0
    print('Número inválido')
if tentativa != jogada:  # anuncia a derrota do usuário
    print(f'GANHEI! Eu pensei no número {jogada} e não no {tentativa}!')
if tentativa == jogada:  # anuncia a vitória do usuário
    print('PARABÉNS! Você conseguiu me vencer!')
