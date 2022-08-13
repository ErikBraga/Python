cont = 0
soma = 0

for c in range(0, 501, 3):  # soma de todos os números ímpares múltiplos de 3
    if c % 2 == 1:  # se o número for ímpar
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
