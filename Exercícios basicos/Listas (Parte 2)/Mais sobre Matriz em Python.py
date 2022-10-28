matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira_coluna = maior_segLinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]  # soma todos os números pares digitados na matriz
        if c == 2:
            terceira_coluna += matriz[l][c]  # soma os números da terceira coluna
        if l == 1:
            maior_segLinha = max(matriz[1])  # soma os números da segunda linha
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_segLinha}.')
