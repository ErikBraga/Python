cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1  # contador de números digitados
    soma += num  # soma de todos os números digitados
print(f'A soma dos {cont} valores foi {soma}!')
