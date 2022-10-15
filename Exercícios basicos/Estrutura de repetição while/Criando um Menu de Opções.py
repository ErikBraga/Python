from time import sleep
opcao = 0
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if 5 < opcao < 1:  # se a opção for maior que 5 e menor que 1 ela é inválida.
        print('Opção inválida. Tente novamente')
    if opcao == 1:
        print(f'A soma entre {p1} + {p2} é {p1 + p2}')
    if opcao == 2:
        print(f'O resultado da multiplicação entre {p1} e {p2} é {p1 * p2}')
    if opcao == 3:  # if para descobrir o maior dos dois números
        if p1 > p2:
            print(f'Entre {p1} e {p2} o maior valor é {p1}')
        elif p2 > p1:
            print(f'Entre {p1} e {p2} o maior valor é {p2}')
        else:  # se os números forem iguais
            print('Os dois números são iguais.')
    if opcao == 4:
        print('Informe os números novamente:')
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    if opcao == 5:
        print('Finalizando...')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre!')

