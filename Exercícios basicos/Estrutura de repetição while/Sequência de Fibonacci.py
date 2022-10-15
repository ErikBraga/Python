print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
print('-=' * 23)
anterior = 0
proxima = 1
soma = 1
cont = 0  # contador de quantas vezes a repetição vai acontecer
while cont < termos:
    print(anterior, end=' → ')
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    cont += 1
print('FIM')
print('-=' * 23)

