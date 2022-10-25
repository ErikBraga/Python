valores = []
for c in range(0, 5):  # laço para adicionar 5 números na lista "valores"
    valores.append(int(input(f'Digite um valor para a {c+1}ª posição: ')))  # adiciona o número digitado na lista "valores"
print('-=' * 20)
print(f'Você digitou os valores {valores}')  # print da lista
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')  # maior valor adicionado na lista
for c, n in enumerate(valores):
    if n == max(valores):  # "n" é cada um dos elementos da lista, se "n" for igual ao maior valor da lista
        print(valores.index(max(valores), c)+1, end='... ')  # mostra as posições que o maior número da lista está, podendo ser mais de uma posição
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')  # menor valor adicionado na lista
for c, n in enumerate(valores):
    if n == min(valores):  # "n" é cada um dos elementos da lista, se "n" for igual ao menor valor da lista
        print(valores.index(min(valores), c)+1, end='... ')  # mostra as posições que o menor número da lista está, podendo ser mais de uma posição
print()
