n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior valor digitado foi {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior valor digitado foi {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor valor digitado foi {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor valor digitado foi {n3}')
