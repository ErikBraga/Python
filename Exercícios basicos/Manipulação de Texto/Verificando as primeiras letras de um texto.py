cidade = str(input('Em que cidade você nasceu? ')).replace('-', ' ').lower().split()  # replace para caso o nome da cidade seja separado com "-"
# o nome da cidade está separado em listas por conta do "split"
print('Analisando se o nome da sua cidade começa com "Santo"...')
if cidade[0] == 'santo':  # analisa se a palavra da primeira lista é apenas "Santo" recusando assim resultados como "Santorini"
    print(f'O nome da sua cidade começa com "Santo".')
else:
    print('O nome da sua cidade não começa com "Santo".')
