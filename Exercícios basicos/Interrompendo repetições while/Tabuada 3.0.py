while True:
    num = int(input('Quer ver a tabuada de qual valor? (0 para encerrar) '))
    print('-' * 30)
    if num <= 0:  # se o número digitado for menor ou igual a 0 o programa é encerrado
        break
    for c in range(1, 11):  # laço de repetição para formar a tabuada
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO.')
