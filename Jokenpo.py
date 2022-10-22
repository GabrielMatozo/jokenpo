from random import choice
from time import sleep

print('\033[0;34m-=*=-' * 10)
print('\033[0;31m               じゃん拳ぽん JANKENPON')
print('                      ✊✋✌')
print('\033[0;34m-=*=-\033[0;32m' * 10)
print('\nJOGO CONTRA O COMPUTADOR INICIADO...\n')

while True:
    opcoes = [1, 2, 3]
    escolhaMaquina = choice(opcoes)

    print('[1] PEDRA✊')
    print('[2] PAPEL✋')
    print('[3] TESOURA✌')
    print('[0] FINALIZAR JOGO')

    while True:
        try:
            escolha = int(input('Escolha sua jogada: '))
            print('\n')
            break
        except ValueError:
            print('\n\033[0;31mDigite uma opção valida!\033[0;32m\n')

    if escolha == 1:
        print('\033[0m-=*=-' * 5)
        print('ESCOLHA DO JOGADOR: ✊')
        sleep(0.5)
        if escolhaMaquina == 1:
            print('ESCOLHA DO COMPUTADOR: ✊')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;33m---EMPATE---\033[0;32m\n')
        elif escolhaMaquina == 2:
            print('ESCOLHA DO COMPUTADOR: ✋')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;31m---VOCE PERDEU---\033[0;32m\n')
        else:
            print('ESCOLHA DO COMPUTADOR: ✌')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;34m---VOCE GANHOU!---\033[0;32m\n')

    elif escolha == 2:
        print('\033[0m-=*=-' * 5)
        print('ESCOLHA DO JOGADOR: ✋')
        sleep(0.5)
        if escolhaMaquina == 1:
            print('ESCOLHA DO COMPUTADOR: ✊')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;34m---VOCE GANHOU!---\033[0;32m\n')
        elif escolhaMaquina == 2:
            print('ESCOLHA DO COMPUTADOR: ✋')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;33m---EMPATE---\033[0;32m\n')
        else:
            print('ESCOLHA DO COMPUTADOR: ✌')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;31m---VOCE PERDEU---\033[0;32m\n')

    elif escolha == 3:
        print('\033[0m-=*=-' * 5)
        print('ESCOLHA DO JOGADOR: ✌')
        sleep(0.5)
        if escolhaMaquina == 1:
            print('ESCOLHA DO COMPUTADOR: ✊')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;31m---VOCE PERDEU---\033[0;32m\n')
        elif escolhaMaquina == 2:
            print('ESCOLHA DO COMPUTADOR: ✋')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;34m---VOCE GANHOU!---\033[0;32m\n')
        else:
            print('ESCOLHA DO COMPUTADOR: ✌')
            print('-=*=-' * 5)
            sleep(0.5)
            print('\n\033[0;33m---EMPATE---\033[0;32m\n')

    elif escolha == 0:
        break
    else:
        print('\n\033[0;31mDigite uma opção valida!\033[0;32m\n')

    sleep(0.7)
