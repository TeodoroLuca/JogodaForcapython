import random
import os
import time
from colorama import*
import pygame

# Sons do jogo para cada etapa do jogo e efeitos 
pygame.init()
som = pygame.mixer.Sound('perdeu.wav')
som2 = pygame.mixer.Sound('aplausos.wav')
som3 = pygame.mixer.Sound('erro.wav')
som4 = pygame.mixer.Sound('normal.wav')
som5 = pygame.mixer.Sound('tormento.wav')
som6 = pygame.mixer.Sound('inferno.wav')
som7 = pygame.mixer.Sound('nightmare.wav')
som8 = pygame.mixer.Sound('letraerrada.wav')
som9 = pygame.mixer.Sound('alerta.wav')
som10 = pygame.mixer.Sound('loading.wav')
som11 = pygame.mixer.Sound('inicio.wav')

#Função sorteadora de palavra do jogo
def escolher_palavra():
    with open("forca.txt") as arquivo:
        palavras = arquivo.readlines()
    palavra = random.choice(palavras).strip()
    return palavra.lower()

#layout do jogo, com desenho da forca atribuindo a quantidade de erros do jogador
def desenhar_forca(erros):# layout da dificuldade normal
    if erros == 1:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=                   |_|            ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 2:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=                 |     |          ||                =-=
                    =-=                 |     |          ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 3:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |          ||                =-=
                    =-=             /_/ |     |          ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 4:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 5:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | |              ||                =-=
                    =-=                 | |              ||                =-=
                    =-=               __| |              ||                =-=
                    =-=              |____|              ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 6:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=               __| | | |__        ||                =-=
                    =-=              |____| |____|       ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
        time.sleep(1)

def desenhar_forca2(erros):#layout da dificuldade tormento
    if erros == 1:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |          ||                =-=
                    =-=             /_/ |     |          ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 2:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                  ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 3:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | |              ||                =-=
                    =-=                 | |              ||                =-=
                    =-=               __| |              ||                =-=
                    =-=              |____|              ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 4:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=               __| | | |__        ||                =-=
                    =-=              |____| |____|       ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
        time.sleep(1)

def desenhar_forca3(erros):#layout da dificuldade inferno
    if erros == 1:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | |              ||                =-=
                    =-=                 | |              ||                =-=
                    =-=               __| |              ||                =-=
                    =-=              |____|              ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
    elif erros == 2:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=               __| | | |__        ||                =-=
                    =-=              |____| |____|       ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
        time.sleep(1)

def desenhar_forca4(erros):#layout da dificuldade nigthmare
    if erros == 1:
        os.system('clear')
        print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                    ||============||                =-=          
                    =-=                    |             ||                =-=
                    =-=                    |             ||                =-=
                    =-=                   _|_            ||                =-=
                    =-=                  /   \           ||                =-=
                    =-=                 | 0 0 |          ||                =-=
                    =-=                  \ - /           ||                =-=
                    =-=               ____|_|____        ||                =-=
                    =-=              / /|     |\ \       ||                =-=
                    =-=             /_/ |     | \_\      ||                =-=
                    =-=                 |_____|          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=                 | | | |          ||                =-=
                    =-=               __| | | |__        ||                =-=
                    =-=              |____| |____|       ||                =-=
                    =-=                                 ||||               =-=
                    =-=                               ========             =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================
                    ''')
        time.sleep(1)

# Atribuições a dificuldade Normal
def jogar():
    palavra = escolher_palavra() #variável que chama a palvra sorteada
    acertos = set() #conjunto vazio de acertos
    erros = 0 # inicia o jogo sem erros kkk logicamente falando 
    letras_digitadas = []# faz uma lista de todas letras já digitadas

    while True: 
        for letra in palavra:
            if letra in acertos:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        if erros == 5:# som de  alerta um erro antes da última tentativa
            som9.play()    
        if erros == 6:# perde o jogo e aparece o layout da derrota
            som9.stop()
            os.system('clear')
            print(Fore.RED,Style.BRIGHT,'''
                        ==========================================================
                        =-=                   VOCÊ PERDEU!                     =-=
                        =-=                    +-------+                       =-=
                        =-=                    |       |                       =-=
                        =-=                  (@-@)     |                       =-=
                        =-=                   |||      |                       =-=
                        =-=    CONDENADO A     |       |    LÁ MUERTE!         =-= 
                        =-=                   | |      |                       =-=
                        =-=                            |                       =-=
                        =-=                           ===                      =-=
                        ==========================================================             
            ''')
            print('A palavra era:', palavra)#mostra a palavra correta
            som.play()# som da derrota 
            time.sleep(2)

            jogar_novamente = input('Deseja jogar novamente? (s/n): ')# jogar novamente ou sair do jogo após a vitória ou derrota
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()

        if set(palavra) == acertos:# ganha o jogo e aparece o layout da vitória
            os.system('clear')
            som9.stop()
            print(Fore.GREEN,Style.BRIGHT)
            print('''
                        ==========================================================
                        =-=                      VOCÊ GANHOU!                  =-= 
                        =-=                                                    =-= 
                        =-=            \     /                                 =-= 
                        =-=             \*-*/                                  =-= 
                        =-=               |                                    =-= 
                        =-=               |                                    =-= 
                        =-=              / \        LIBERDADE, LIBERDADE!      =-= 
                        =-=             /   \                                  =-=                     
                        =-=                                                    =-= 
                        ==========================================================
            ''')
            som2.play()# som de aplausos pela vitória
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()

        letra = (input('\t    Digite uma letra: '))
        som3.play()

        if letra in letras_digitadas:# retorna a mensagem de letra repetida 
            print('Vocẽ já digitou: ', letra)

        else:
            letras_digitadas += letra
            if letra in acertos or letra in palavra:
                acertos.add(letra)
                print('Letras Digitadas: ', letras_digitadas)
            
            else: 
                som8.play() 
                erros += 1
                desenhar_forca(erros)
                print('letras digitadas: ', letras_digitadas)

# Atribuições a dificuldade Tormento
def jogar2():
    palavra = escolher_palavra()
    acertos = set()
    erros = 0
    letras_digitadas = []

    while True:
        for letra in palavra:
            if letra in acertos:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        if erros == 3:
            som9.play()
        if erros == 4:
            som9.stop()
            os.system('clear')
            print(Fore.RED,Style.BRIGHT,'''
                        ==========================================================
                        =-=                   VOCÊ PERDEU!                     =-=
                        =-=                    +-------+                       =-=
                        =-=                    |       |                       =-=
                        =-=                  (@-@)     |                       =-=
                        =-=                   |||      |                       =-=
                        =-=    CONDENADO A     |       |    LÁ MUERTE!         =-= 
                        =-=                   | |      |                       =-=
                        =-=                            |                       =-=
                        =-=                           ===                      =-=
                        ==========================================================             
            ''')
            print('A palavra era:', palavra)
            som.play()
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()

        if set(palavra) == acertos:
            os.system('clear')
            som9.stop()
            print(Fore.GREEN,Style.BRIGHT)
            print('''
                        ==========================================================
                        =-=                      VOCÊ GANHOU!                  =-= 
                        =-=                                                    =-= 
                        =-=            \     /                                 =-= 
                        =-=             \*-*/                                  =-= 
                        =-=               |                                    =-= 
                        =-=               |                                    =-= 
                        =-=              / \        LIBERDADE, LIBERDADE!      =-= 
                        =-=             /   \                                  =-=                     
                        =-=                                                    =-= 
                        ==========================================================
            ''')
            som2.play()
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')        
                exit()
        letra = (input('\t    Digite uma letra: '))
        som3.play()

        if letra in letras_digitadas:
            print("vocẽ já digitou: ", letra)

        else:
            letras_digitadas += letra
            if letra in acertos or letra in palavra:
                acertos.add(letra)
                print('letras digitadas: ', letras_digitadas)
            
            else: 
                som8.play() 
                erros += 1
                desenhar_forca2(erros)
                print('letras digitadas: ', letras_digitadas)

# Atribuições a dificuldade inferno
def jogar3():
    palavra = escolher_palavra()
    acertos = set()
    erros = 0
    letras_digitadas = []

    while True:
        for letra in palavra:
            if letra in acertos:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        if erros == 1:
            som9.play()
        if erros == 2:
            som9.stop()
            os.system('clear')
            print(Fore.RED,Style.BRIGHT,'''
                        ==========================================================
                        =-=                   VOCÊ PERDEU!                     =-=
                        =-=                    +-------+                       =-=
                        =-=                    |       |                       =-=
                        =-=                  (@-@)     |                       =-=
                        =-=                   |||      |                       =-=
                        =-=    CONDENADO A     |       |    LÁ MUERTE!         =-= 
                        =-=                   | |      |                       =-=
                        =-=                            |                       =-=
                        =-=                           ===                      =-=
                        ==========================================================             
            ''')
            print('A palavra era:', palavra)
            som.play()
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()

        if set(palavra) == acertos:
            os.system('clear')
            som9.stop()
            print(Fore.GREEN,Style.BRIGHT)
            print('''
                        ==========================================================
                        =-=                      VOCÊ GANHOU!                  =-= 
                        =-=                                                    =-= 
                        =-=            \     /                                 =-= 
                        =-=             \*-*/                                  =-= 
                        =-=               |                                    =-= 
                        =-=               |                                    =-= 
                        =-=              / \        LIBERDADE, LIBERDADE!      =-= 
                        =-=             /   \                                  =-=                     
                        =-=                                                    =-= 
                        ==========================================================
            ''')
            som2.play()
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()
        letra = (input('\t    Digite uma letra: '))
        som3.play()

        if letra in letras_digitadas:
            print("vocẽ já digitou: ", letra)

        else:
            letras_digitadas += letra
            if letra in acertos or letra in palavra:
                acertos.add(letra)
                print('letras digitadas: ', letras_digitadas)
            
            else: 
                som8.play() 
                erros += 1
                desenhar_forca3(erros)
                print('letras digitadas: ', letras_digitadas)

# Atribuições a dificuldade Nightmare
def jogar4():
    palavra = escolher_palavra()
    acertos = set()
    erros = 0
    letras_digitadas = []
    
    while True:
        for letra in palavra:
            if letra in acertos:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        if erros ==0:
            som9.play()
        if erros == 1:
            os.system('clear')
            print(Fore.RED,Style.BRIGHT,'''
                        ==========================================================
                        =-=                   VOCÊ PERDEU!                     =-=
                        =-=                    +-------+                       =-=
                        =-=                    |       |                       =-=
                        =-=                  (@-@)     |                       =-=
                        =-=                   |||      |                       =-=
                        =-=    CONDENADO A     |       |    LÁ MUERTE!         =-= 
                        =-=                   | |      |                       =-=
                        =-=                            |                       =-=
                        =-=                           ===                      =-=
                        ==========================================================             
            ''')
            print('A palavra era:', palavra)
            som.play()
            time.sleep(2)

            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()

        if set(palavra) == acertos:
            som9.stop()
            os.system('clear')
            print(Fore.GREEN,Style.BRIGHT)
            print('''
                        ==========================================================
                        =-=                      VOCÊ GANHOU!                  =-= 
                        =-=                                                    =-= 
                        =-=            \     /                                 =-= 
                        =-=             \*-*/                                  =-= 
                        =-=               |                                    =-= 
                        =-=               |                                    =-= 
                        =-=              / \        LIBERDADE, LIBERDADE!      =-= 
                        =-=             /   \                                  =-=                     
                        =-=                                                    =-= 
                        ==========================================================
            ''')
            som2.play()
            time.sleep(2)
            
            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() == "s":
                menu()
            else:
                os.system('clear')
                print("=-=-=-=-= Jogo Encerrado =-=-=-=-=")
                print("=-=-=-=-= Obrigado por Jogar =-=-=-=-=")
                time.sleep(2)
                os.system('clear')
                exit()
        letra = (input('\t    Digite uma letra: '))
        som3.play()

        if letra in letras_digitadas:
            print("vocẽ já digitou: ", letra)

        else:
            letras_digitadas += letra
            if letra in acertos or letra in palavra:
                acertos.add(letra)
                print('letras digitadas: ', letras_digitadas)
            
            else: 
                som8.play() 
                erros += 1
                desenhar_forca4(erros)
                print('letras digitadas: ', letras_digitadas)  

def carregar(): #Função que inicializa o carregamento do jogo
    print(Fore.LIGHTCYAN_EX,Style.BRIGHT)
    os.system('clear')
    print(''' 
                    ==========================================================                  
                    ==========================================================
                    =-=                                                    =-=
                    =-=                          ||============||          =-=          
                    =-=                          |             ||          =-=
                    =-=                          |             ||          =-=
                    =-=                         _|_            ||          =-=
                    =-=                        /   \           ||          =-=
                    =-=                       | @ @ |          ||          =-=
                    =-=                        \ - /           ||          =-=
                    =-=                     ____|_|____        ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    |_||_____||_|       ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                     __| | | |__        ||          =-=
                    =-=                    |____| |____|       ||          =-=
                    =-=                                       ||||         =-=
                    =-=                                     ========       =-=
                    =-=                                                    =-=
                    =-=  loading =                   Produced by L.Teodoro =-=
                    ========================================================== ''')
    time.sleep(1), os.system('clear')

    print('''    
                    ==========================================================               
                    ==========================================================
                    =-=                                                    =-=
                    =-=                          ||============||          =-=          
                    =-=                          |             ||          =-=
                    =-=                          |             ||          =-=
                    =-=                         _|_            ||          =-=
                    =-=                        /   \           ||          =-=
                    =-=                       | @ @ |          ||          =-=
                    =-=                        \ - /           ||          =-=
                    =-=                     ____|_|____        ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    |_||_____||_|       ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                     __| | | |__        ||          =-=
                    =-=                    |____| |____|       ||          =-=
                    =-=                                       ||||         =-=
                    =-=                                     ========       =-=
                    =-=                                                    =-=
                    =-=  loading ==                  Produced by L.Teodoro =-=
                    ========================================================== ''')
    time.sleep(1),os.system('clear')

    print('''        
                    ==========================================================           
                    ==========================================================
                    =-=                                                    =-=
                    =-=                          ||============||          =-=          
                    =-=                          |             ||          =-=
                    =-=                          |             ||          =-=
                    =-=                         _|_            ||          =-=
                    =-=                        /   \           ||          =-=
                    =-=                       | @ @ |          ||          =-=
                    =-=                        \ - /           ||          =-=
                    =-=                     ____|_|____        ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    | ||     || |       ||          =-=
                    =-=                    |_||_____||_|       ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                     __| | | |__        ||          =-=
                    =-=                    |____| |____|       ||          =-=
                    =-=                                       ||||         =-=
                    =-=                                     ========       =-=
                    =-=                                                    =-=
                    =-=  loading ===                 Produced by L.Teodoro =-=
                    ========================================================== ''')
    som10.play()
    time.sleep(1), os.system('clear')

# Inicializa o Menu inicial do jogo com suas opções
def menu():
    print(Fore.LIGHTCYAN_EX,Style.BRIGHT)
    os.system('clear')
    print('''      
                    =-=-=-=-=-=-=-= BEM VINDO AO JOGO DA FORCA =-=-=-=-=-=-=-=             
                    ==========================================================
                    =-=                                                    =-=
                    =-=                          ||============||          =-=          
                    =-=                          |             ||          =-=
                    =-=                          |             ||          =-=
                    =-=                         _|_            ||          =-=
                    =-=                        /   \           ||          =-=
                    =-=                       | @ @ |          ||          =-=
                    =-=                        \ - /           ||          =-=
                    =-=                     ____|_|____        ||          =-=
                    =-= 1.Jogar            | ||     || |       ||          =-=
                    =-= 2.Instruções       | ||     || |       ||          =-=
                    =-= 3.Sair             |_||_____||_|       ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                       | | | |          ||          =-=
                    =-=                     __| | | |__        ||          =-=
                    =-=                    |____| |____|       ||          =-=
                    =-=                                       ||||         =-=
                    =-=                                     ========       =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ========================================================== ''')
    som11.play(20)

    opcao = input('''\t\t    Digite uma Opção: ''')
    som11.stop()
    som3.play()

    # Atribui funcionalidade as opções do menu inicial = menu
    if opcao == '1':
        menu_dificuldade()
    elif opcao == '2':
        print('Instruções:')
        print('O objetivo do jogo é adivinhar a palavra secreta, letra por letra.')
        print('''Você tem um número limitado de tentativas, então escolha suas letras sabiamente.
            Escolha a Dificuldade, e Liberte-se ou Morra. 
            1 - Normal    (6 tentativas)
            2 - Tormento  (4 tentativas)
            3 - Inferno   (2 tentativas)
            4 - Nightmare (1 tentativa)
              ''')
        print('Boa Sorte!')
        opcao = input('Digite uma opção: ')
        if opcao == '1':
            menu_dificuldade()
        elif opcao == '3':
            menu()
        else:
            print('Opção Invalida! Tente novamente.')
            opcao = input('''    Digite uma Opção: ''')
            if opcao == '1':
                menu_dificuldade()
            elif opcao == '3':
                menu()
                
    elif opcao == '3':
        os.system('clear')
        print("===== Jogo Encerrado =====")
        print("===== Obrigado por Jogar =====")
        time.sleep(2)
        os.system('clear')
        exit()
        
# Inicializa menu de opções de dificuldades que define a quantidade de tentativas do jogador
def menu_dificuldade():
    os.system('clear')
    print(Fore.LIGHTCYAN_EX,Style.BRIGHT)
    print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                  ||============||                  =-=
                    =-=                  |             ||                  =-=
                    =-=                  |             ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=     1 - Normal                 ||                  =-=
                    =-=     2 - Tormento               ||                  =-=
                    =-=     3 - Inferno                ||                  =-=
                    =-=     4 - Nightmare              ||                  =-=            
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                               ||||                 =-=
                    =-=                             ========               =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================''')
    dificuldade = input('\t\t    Dificuldade: ')
    os.system('clear')
    print(Fore.LIGHTCYAN_EX,Style.BRIGHT)
    print('''
                    ==========================================================
                    =-=                                                    =-=
                    =-=                  ||============||                  =-=
                    =-=                  |             ||                  =-=
                    =-=                  |             ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=            
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                                ||                  =-=
                    =-=                               ||||                 =-=
                    =-=                             ========               =-=
                    =-=                                                    =-=
                    =-=                                                    =-=
                    ==========================================================''')
    
    # Atribui a quantidade de tentativas as opções da dificuldade
    if dificuldade == "1":
        som4.play()
        jogar()
    elif dificuldade == "2":
        som5.play()
        jogar2()
    elif dificuldade == "3":
        som6.play()
        jogar3()
    elif dificuldade == "4":
        som7.play()
        time.sleep(2)
        jogar4()
    else:
        print("Dificuldade inválida. Tente novamente.")
        time.sleep(1)
        menu_dificuldade()

carregar()
menu()
