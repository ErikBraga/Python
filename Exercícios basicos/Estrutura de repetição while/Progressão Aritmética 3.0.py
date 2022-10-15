print('Gerador de PA')
print('-=' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = termos = 0
while cont != 10:
    print(primeiro_termo, end=' → ')
    primeiro_termo += razao
    cont += 1
print('PAUSA')
cont = 0  # contador volta para 0 após a primeira parte do programa
total_termos = 10  # variável para soma total de termos
while cont <= termos:
    termos = int(input('Quantos termos você quer mostrar a mais? '))  # mais termos começando pelo último calculado
    cont = 0  # contador volta a ser 0 para a repetição funcionar devidamente
    if termos == 0:  # se o usuário digitar 0 na variável "termos" o programa é finalizado
        break
    while cont < termos:  # enquanto contador for menor que o termo escolhido pelo usuário
        print(primeiro_termo, end=' → ')
        primeiro_termo += razao
        cont += 1
        total_termos += 1  # contador de total de termos para informação no final do programa
    if cont == termos:  # quando o contador atingir o mesmo valor que o termo digitado pelo usuário, o loop recomeça
        print('PAUSA')
print(f'Progressão finalizada com {total_termos} termos mostrados.')
