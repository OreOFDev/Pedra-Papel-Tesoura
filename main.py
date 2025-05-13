# importo random pra fazer as escolhas da AI e chamo ele de r
import random as r

# printo as opções para a pessoa
print("""
pd = Pedra
pp = Papel
t = tesoura
""")

# e = Escolha, pergunto pra ele qual escolha ele vai ter pd, pp ou t
e = input("Digite sua escolha: ")

# t = tudo vai ser usado pra AI escolher a opcao
t = ["Pedra", "Papel", "Tesoura"]

# se a escolha for igual a pd
if e == "pd":

    # printar oque a pessoa escolheu
    print("Voce escolheu Pedra!")

    # aqui a IA escolhe qualquer opcao da lista t usando o modulo random
    AI = r.choice(t)

    # se a opcao da IA for papel
    if AI == "Papel":

        # printar que a IA ganhou
        print(f"O Computador Venceu Escolhendo {AI}")

    # se a opcao da IA for pedra
    elif AI == "Pedra":

        # printo que o jogo empatou
        print(f"O Jogo Empatou Com Os Dois Escolhendo {AI}")

    # se a opcao da IA for tesoura
    elif AI == "Tesoura":

        # printar oq o computador escolheu
        print(f"O Computador Escolheu {AI}")
        
        # printar que voce ganhou escolhendo {e}
        print(f"Voce Venceu Escolhendo {e}")

#se a pessoa escolher pp = papel
elif e == "pp":

    # printar oque a pessoa escolheu
    print("Voce escolheu Papel!")

    # aqui a IA escolhe qualquer opcao da lista t usando o modulo random
    AI = r.choice(t)

    # se a opcao da IA for tesoura
    if AI == "Tesoura":

        # printar que a IA ganhou
        print(f"O Computador Venceu Escolhendo {AI}")

    # se a opcao que a IA escolheu for papel 
    elif AI == "Papel":

        # printo que o jogo empatou
        print(f"O Jogo Empatou Com Os Dois Escolhendo {AI}")

    # se a opcao que a IA escolheu for Pedra 
    elif AI == "Pedra":

        # printar oq o computador escolheu
        print(f"O Computador Escolheu {AI}")

        # printar voce venceu escolhendo {e}
        print(f"Voce Venceu Escolhendo {e}")


# se a pessoa escolher t = tesoura
elif e == "t":

    # printar oque a pessoa escolheu
    print("Voce escolheu Tesoura!")

    # aqui a IA escolhe qualquer opcao da lista t usando o modulo random
    AI = r.choice(t)

    # se a IA escolher pedra
    if AI == "Pedra":

        # printar que a IA ganhou
        print(f"O Computador Venceu Escolhendo {AI}")

    # se a IA escolher tesoura
    elif AI == "Tesoura":

        # printar que o jogo empatou
        print(f"O Jogo Empatou Com Os Dois Escolhendo {AI}")

    # se a IA escolher papel
    elif AI == "Papel":

        # printar oque a IA escolheu
        print(f"O Computador Escolheu {AI}")

        # printar voce venceu
        print(f"Voce Venceu Escolhendo {e}")
