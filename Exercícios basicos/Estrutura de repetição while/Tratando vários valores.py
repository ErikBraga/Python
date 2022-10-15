soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num  # soma de todos os números digitados na variável "num"
    cont += 1  # contador de quantos números foram digitados na variável "num"
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
