num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')  # conversão para binário excluindo o "0b"
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')  # conversão para octal excluindo o "0o"
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')  # conversão para hexadecimal excluindo o "0x"
else:
    print('Número inválido.')
