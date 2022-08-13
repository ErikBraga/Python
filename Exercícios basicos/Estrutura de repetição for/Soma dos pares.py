soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro: '))
    if num % 2 == 0:  # se o número for par
        soma += num  # soma dos números pares
        cont += 1  # contador de quantos números pares foram digitados
if cont == 1:  # se tiver apenas um número par
    print(f'O único número par fornecido foi {soma}.')
else:
    print(f'A soma dos {cont} números pares é {soma}.')
