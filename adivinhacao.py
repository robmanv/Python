import random
from decimal import Decimal

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    #python builtin functions não precisa ser importada mas o random sim (efetuar import de módulo)


    # numero_secreto = 42
    # numero_secreto = int(random.random() * 100)
    # numero_secreto = round(random.random() * 100)
    numero_secreto = round(random.randrange(1,101))
    print("numero secreto é:", numero_secreto)
    valor = 123456.32

    print("Valor = R$ {:f}".format(valor))
    print("Valor = R$ {:.2f}".format(valor))
    print("Valor = R$ {:12.2f}".format(valor))
    print("Valor = R$ {:012.2f}".format(valor))
    print("Valor = R$ {:012d}".format(int(valor)))

    print("Data = {:02d}/{:02d}/{:04d}".format(20, 2, 1982))

    #Divisao inteira, trunca basicamente
    print(3 // 2)

    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # while(rodada <= total_de_tentativas):
    # for rodada in range(1, total_de_tentativas + 1, 2):  --> pula de 2 em 2
    for rodada in range(1, total_de_tentativas + 1):

        # print("Tentativa", rodada, "de", total_de_tentativas)
        # print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute)
        numero = int(chute)

        if(numero < 1 or numero > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == numero
        menor =  numero < numero_secreto
        maior =  numero > numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif(maior):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - numero)
        pontos = pontos - pontos_perdidos

        print ("Pontuacao atual: ", pontos)
        rodada = rodada + 1

    print("Fim do jogo")

    # nome = "Nico"
    # sobrenome = "Steppat"
    # print(nome, sobrenome)
    # print(nome + sobrenome)
    # print(10 * "20")

if (__name__ == "__main__"):
    jogar()