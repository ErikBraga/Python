from random import choice
from time import sleep

computador = choice(['Pedra', 'Papel', 'Tesoura'])  # jogada do computador
decisao = True  # variável para usar mais tarde
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))  # escolha da jogada
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 10)
if jogador == 0 and computador == 'Pedra' or computador == 'Papel' or computador == 'Tesoura':  # se o jogador escolher "Pedra"
    jogador = 'Pedra'
    decisao = 'EMPATE'  # decisão recebe "EMPATE" se o computador tiver escolhido "Pedra" também
    if computador == 'Papel':
        decisao = 'COMPUTADOR VENCE'
    elif computador == 'Tesoura':
        decisao = 'JOGADOR VENCE'
elif jogador == 1 and computador == 'Pedra' or computador == 'Papel' or computador == 'Tesoura':  # se o jogador escolher "Papel"
    jogador = 'Papel'
    decisao = 'JOGADOR VENCE'  # decisão recebe "JOGADOR VENCE" se o computador tiver escolhido "Pedra"
    if computador == 'Papel':
        decisao = 'EMPATE'
    elif computador == 'Tesoura':
        decisao = 'COMPUTADOR VENCE'
elif jogador == 2 and computador == 'Pedra' or computador == 'Papel' or computador == 'Tesoura':  # se o jogador escolher "Tesoura"
    jogador = 'Tesoura'
    decisao = 'COMPUTADOR VENCE'  # decisão recebe "COMPUTADOR VENCE" se o computador tiver escolhido "Pedra"
    if computador == 'Papel':
        decisao = 'JOGADOR VENCE'
    elif computador == 'Tesoura':
        decisao = 'EMPATE'
else:
    print('Jogada inválida.')
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('-=' * 10)
print(decisao)
