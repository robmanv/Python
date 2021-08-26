import random

def jogar():

    imprimir_cabecalho()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = obter_chute()

        if(chute in palavra_secreta):
            letras_acertadas = marcar_chute_correto(letras_acertadas, palavra_secreta, chute)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        # posicao = palavra_secreta.find(chute)
        # print("posição:", posicao)

        print("jogando ...")

    if(acertou):
        imprimir_mensagem_vencedor()

    if(enforcou):
        imprimir_mensagem_perdedor(palavra_secreta)

def imprimir_cabecalho():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
        # print(linha, end="\n")

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    # print(palavras)
    print(palavra_secreta)

    # type(palavra_secreta)

    return palavra_secreta

def inicializar_letras_acertadas(palavra_secreta):
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    letras_acertadas2 = ["_" for letra in palavra_secreta]

    return letras_acertadas

def obter_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()

    return chute

def marcar_chute_correto(letras_acertadas, palavra_secreta, chute):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

    return letras_acertadas

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    # Temos o TUPPLE, lista que não pode mudar, ao invés de colchete, coloco parenteses
    #lista_tupple = (1, 2, 3, 4, 5)

    # lista_normal = []
    # lista_normal.append("banana")
    # lista_normal.append("abacaxi")

    # lista_tupple_convertida = tuple(lista_normal)
    # lista_normal_convertida = list(lista_tupple_convertida)

    # print(lista_normal_convertida)
    # print(lista_tupple_convertida)


    # palavra_secreta = input("Digita a palavra secreta:").upper()

    # with open("palavras.txt") as arquivo:
    #     for linha in arquivo:
    #         print(linha)

    # OU

    #LIST COMPREHENSION
    # inteiros = [1, 3, 4, 5, 7, 8, 9]
    # pares = []
    # for numero in inteiros:
    #     if numero % 2 == 0:
    #         pares.append(numero)
    #
    # # OU
    # inteiros = [1, 3, 4, 5, 7, 8, 9]
    # pares = [x for x in inteiros if x % 2 == 0]


# se rodo diretamente a forca, ou seja, ela é a main
if (__name__ == "__main__"):
    jogar()

