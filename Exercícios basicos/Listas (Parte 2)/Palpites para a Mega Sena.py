from random import randint
from time import sleep
jogos = []
temp = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
while len(jogos) < quantidade:
    num = randint(1, 60)
    if num not in temp:
        temp.append(num)  # se o número gerado não estiver na lista "temp" ele é adicionado na lista "temp"
    if len(temp) == 6:  # quando a lista "temp" chega em 6 números
        temp.sort()  # organiza a lista "temp" em ordem crescente
        jogos.append(temp[:])  # adiciona uma cópia da lista "temp" na lista "jogos"
        temp.clear()  # limpa a lista "temp" para receber novos números
print('-=' * 3, f'  SORTEANDO {quantidade} JOGOS  ', '-=' * 3)
for n, j in enumerate(jogos):
    print(f'Jogo {n+1}: {j}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
