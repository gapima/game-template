import random


def jogar_advinhacao():
    banner = """
    ************************************
    * Bem-vindo ao Jogo da Adivinhação *
    ************************************
    """

    print(banner)

    numero_secreto = random.randrange(1,100)
    total_de_tentativas = 0
    pontos = 1000

    rodada = 1

    print("(1) Facil  (2) Medio  (3) Dificil)")
    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range (1,total_de_tentativas + 1):

        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute = input("Digite o número entre 1 e 100: ")
        chuteint = int(chute)
        print(chuteint)


        if (chuteint< 1 or chuteint > 100):
            print("Voce deve digitar um numero entre 1 a 100")
            continue

        acertou = numero_secreto == chuteint
        errou_devser_menor = chuteint > numero_secreto
        errou_devser_maior = chuteint < numero_secreto



        if acertou:
            print("Você acertou e fez {} pontos!". format(pontos))
            break

        else:
            if errou_devser_menor:
                print("O numero informado é maior que o numero secreto.")

            elif(errou_devser_maior):
                print("O numero informado é menor que o numero secreto.")
                pontos_perdidos = abs(numero_secreto - chuteint)
                pontos = pontos - pontos_perdidos



    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar_advinhacao()
