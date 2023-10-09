import adivinhacao_alura
import forca

def escolhe_jogo():
    print("********************************")
    print("*******Escolha seu jogo!********")
    print("********************************")

    print("(1) Forca")
    print("(2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao_alura.jogar()
    print("Fim de Jogo")

if(__name__ == "__main__"):
    escolhe_jogo()