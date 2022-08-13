primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao  # calculo do décimo termo da PA
for c in range(primeiro_termo, decimo + 1, razao):
    print(primeiro_termo, end=' → ')
    primeiro_termo += razao
print('ACABOU')
