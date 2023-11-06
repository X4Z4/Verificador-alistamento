from time import sleep
print('hj vc vai saber se precisa se alistar')
sleep(2)
s= input('primeiro de tudo,você é homem ou mulher?')
if s=='homem':
    n = input('qual seu nome?: ')
    print('hoje vamos descobrir se vc ainda tem pendencias {}'.format(n))
    a = int(input('que ano vc nasceu: '))
    i = 2022 - a
    o = input('vc ja se alistou?')
    if i > 18 and o == 'sim':
        print('parabens não lhe restam pendencias')

    if i > 18 and o == 'não':
        ap= i-18
        print('trate de se alistar imediatamente, você esta em pendencia com o governo')
        print('ja se passaram {} anos'.format(ap))
    elif i > 18 and 18 - i == 1 and o == 'não':
        an = 18 - 1
        print('ainda não chegou seu momento de servir mas fique de olho esta chegando')
        print('faltam exatamente {} ano'.format(an))


    elif i < 18 :
        an = 18-1
        print('ainda não chegou seu momento de servir mas fique de olho esta chegando')
        print('faltam exatos {} anos'.format(an))

elif s=='mulher':
    n=input('Qual seu nome?')
    print('então senhora {}, você não precisa se alistar mas vc pode se quiser'.format(n))
