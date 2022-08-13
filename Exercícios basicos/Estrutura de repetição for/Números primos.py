num = int(input('Digite um número: '))
divisores = 0
for c in range(1, num + 1):
    if num % c == 0:  # se "num" dividido por "c" igual a 0
        divisores += 1
print(f'O número {num} foi divisível {divisores} vezes')
if divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
