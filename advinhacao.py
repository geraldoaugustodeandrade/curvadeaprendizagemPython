import random

def advinhacao():
    print (" ********************************* ")
    print ( " Bem vindo ao jogo de advinhacao! ")
    print (" ********************************* ")

    ## Variaveis do jogo de advinhação
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3

    print (" Olá, tudo bom ? Qual o nivel de dificuldade que você deseja ? ")
    print (" (1) Facil (2) Medio (3) Dificil " )

    nivel = int(input(" Escolha um nivel: "))
    if nivel == 1:
        total_de_tentativas = 16
    elif nivel == 2:
        total_de_tentativas= 11
    else:
        total_de_tentativas= 6

    ## Comparação das variaveis 'numero_secreto' e 'numero_usuario'
    for rodada in range (1,21):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        numero_usuario = int( input("Digite o seu número: "))
        print (" Você digitou o numero:",numero_usuario)
        if (numero_secreto) == (numero_usuario):
            print(" Você acertou, parabéns! ")
            break
        else:
            if (numero_usuario > numero_secreto):
                print(" Tente novamente, seu palpite foi maior que o numero secreto! ")
            elif (numero_usuario < numero_secreto):

                rodada = rodada + 1

                print (" Tente novamente, seu palpite foi menor que o numero secreto")

        print (" Fim de jogo! ")
if(__name__ == "__main__"):
    advinhacao()


