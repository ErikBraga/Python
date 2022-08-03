cidade = str(input('Em que cidade você nasceu? ')).replace('-', ' ').lower().split()
print('Analisando se o nome da sua cidade começa com "Santo"...')
if cidade[0] == 'santo':
    print(f'O nome da sua cidade começa com "Santo".')
else:
    print('O nome da sua cidade não começa com "Santo".')
