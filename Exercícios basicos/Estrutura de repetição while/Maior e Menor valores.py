maior = menor = cont = total = 0
continuar = ''
while continuar != 'N':  # enquanto "continuar" for diferente de "N (não)" a repetição vai continuar acontecendo
    num = int(input('Dgite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # [0] para pegar apenas a primeira letra digitada (S ou N)
    cont += 1  # contador de quantos números vão ser digitados pelo usuário
    total += num  # soma de todos os números digitados pelo usuário
    if cont == 1:
        maior = num
        menor = num
    else:  # else para descobrir o maior e menor valor digitado pelo usuário
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} números e a média foi {total / cont:.2f}')
print(f'O maior valor foi de {maior} e o menor foi {menor}')
