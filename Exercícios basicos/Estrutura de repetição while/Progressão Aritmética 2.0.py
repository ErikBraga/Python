print('Gerador de PA')  # gerador de progressão aritmética
print('-=' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont != 10:
    print(primeiro_termo, end=' → ')
    primeiro_termo += razao
    cont += 1
print('FIM')
