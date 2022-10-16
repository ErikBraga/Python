from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont_vitorias = 0  # contador de quantas vitórias o usuário teve
while True:
    n_computador = randint(0, 10)  # gerador do número escolhido pelo computador
    n_usuario = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = n_usuario + n_computador  # soma para descobrir se o número é ímpar ou par
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    if soma % 2 == 0:  # se a soma for par
        print(f'Você jogou {n_usuario} e o computador {n_computador}. Total de {soma} DEU PAR')
        print('-' * 30)
        if par_impar == 'I':  # se o jogador tiver escolhido ímpar ele perde
            print('Você PERDEU!')
            print('=-' * 15)
            break
        else:  # se o jogador tiver escolhido par ele ganha
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont_vitorias += 1
        print('=-' * 15)
    elif soma % 2 == 1:  # se a soma for ímpar
        print(f'Você jogou {n_usuario} e o computador {n_computador}. Total de {soma} DEU ÍMPAR')
        print('-' * 30)
        if par_impar == 'P':  # se o jogador tiver escolhido par ele perde
            print('Você PERDEU!')
            print('=-' * 15)
            break
        else:  # se o jogador tiver escolhido par ele ganha
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont_vitorias += 1
        print('=-' * 15)
if cont_vitorias == 1:  # if para não ficar no plural se o contador tiver apenas uma vitória
    print(f'GAME OVER! Você venceu {cont_vitorias} vez.')
else:
    print(f'GAME OVER! Você venceu {cont_vitorias} vezes.')
