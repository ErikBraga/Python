num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 11)
for n in range(1, 10+1):
    print(f'{num} x {n:2} = {num*n}')
print('-' * 11)
