import random 

while True:
    num_aleatorio = random.randint(1, 9)

    resposta = input("Adivinhe o número (1-9) ou digite 'sair' para encerrar o jogo: ")
    
    if resposta == "sair":
        print("Obrigado por jogar!")
        break
    
    if int(resposta) == num_aleatorio:
        print("Parabéns! Você acertou o número.")
    elif int(resposta) < num_aleatorio:
        print("Tente novamente! O número é maior.")
    else:
        print("Tente novamente! O número é menor.")
