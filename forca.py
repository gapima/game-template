
import forca
import advinhacao

def escolhe_jogo():
    banner = """
    ************************************
    ******* Escolha o seu jogo!*********
    ************************************
    """

    print(banner)

    print("(1)Forca ou (2)Advinhacao")
    jogo = int(input("Escolha: "))

    if(jogo == 1):
        print("Jogando forca!")
        forca.jogo_forca()

    elif(jogo == 2):
        print("Jogando Advinhacao!")
        advinhacao.jogar_advinhacao()

if (__name__ == "__main__"):
    escolhe_jogo()
