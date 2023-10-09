import random

def jogar():
    print("********************************")
    print("Bem Vido ao jogo de adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Escolha um nível válido!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um numero: ")
        print("Você digitou: " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!!!".format(format(pontos)))
            break
        else:
            if(maior):
                print("Você errou :(, o seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você errou :(, o seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()