lista = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite o {n}o. valor: '))
    if num % 2 == 0:  # se o número for par
        lista[0].append(num)  # adiciona os números pares em uma lista dentro de "lista"
    else:
        lista[1].append(num)  # adiciona os números ímpares em outra lista dentro de "lista"
print('-=' * 30)
lista[0].sort()  # organiza os números pares em ordem crescente
lista[1].sort()  # organiza os números ímpares em ordem crescente
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
