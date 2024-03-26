
t = int(input("Numero de testes: "))




for i in range(t):
    
    escolhas = input("Escolhas de Sheldon e Raj: ")

    escolhas_lista = escolhas.split()

    escolha_sheldon = escolhas_lista[0]
    escolha_raj = escolhas_lista[1]

    
    if escolha_raj != escolha_sheldon:

        if escolha_sheldon == "pedra":
            if escolha_raj == "papel":
                vencedor = 0
            elif escolha_raj == "tesoura":
                vencedor = 1
            elif escolha_raj == "lagarto":
                vencedor = 1
            else:
                vencedor = 0

        elif escolha_sheldon == "papel":
            if escolha_raj == "pedra":
                vencedor = 1
            elif escolha_raj == "tesoura":
                vencedor = 0
            elif escolha_raj == "lagarto":
                vencedor = 0
            else:
                vencedor = 1

        elif escolha_sheldon == "tesoura":
            if escolha_raj == "pedra":
                vencedor = 0
            elif escolha_raj == "papel":
                vencedor = 1
            elif escolha_raj == "lagarto":
                vencedor = 1
            else:
                vencedor = 0

        elif escolha_sheldon == "lagarto":
            if escolha_raj == "pedra":
                vencedor = 0
            elif escolha_raj == "papel":
                vencedor = 1
            elif escolha_raj == "tesoura":
                vencedor = 0
            else:
                vencedor = 1

        elif escolha_sheldon == "Spock":
            if escolha_raj == "pedra":
                vencedor = 1
            elif escolha_raj == "papel":
                vencedor = 0
            elif escolha_raj == "tesoura":
                vencedor = 1
            else:
                vencedor = 0

        if vencedor == 0:
            print("Raj trapaceou!")
        else:
            print("Bazinga!")

    else:
        print("De novo!")