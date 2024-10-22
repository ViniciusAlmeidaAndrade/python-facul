jogar_novamente = 'sim' 
jogadas = 0
jogadores = 2
max_jogadas = 9
vitoria = False
j_velha = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def corpo():
    print("     0   1   2")
    print("     -----------")
    for i in range(3):
        print(f" {i}:  {j_velha[i][0]} | {j_velha[i][1]} | {j_velha[i][2]}")
        if i < 2:
            print("     -----------")

def jogador1():
    global jogadas, jogadores, vitoria, max_jogadas, j_velha

    if jogadores == 2 and jogadas < max_jogadas:
        while True:
            try:
                l = int(input('Linha..: '))
                c = int(input('Coluna..: '))

                if l < 0 or l > 2 or c < 0 or c > 2:
                    print("Por favor insira uma posição entre 0 e 2")
                    continue

                if j_velha[l][c] != " ":
                    print("Erro! espaço já está sendo utilizado.")
                    continue

                j_velha[l][c] = 'X'
                jogadas += 1
                jogadores = 1
                break
            except ValueError:
                print("Por favor insira uma posição: 0 ou 1")

def jogador2():
    global jogadas, jogadores, vitoria, max_jogadas, j_velha

    if jogadores == 1 and jogadas < max_jogadas:
        while True:
            try:
                l = int(input('Linha..: '))
                c = int(input('Coluna..: '))

                if l < 0 or l > 2 or c < 0 or c > 2:
                    print("Linha e coluna devem estar entre 0 e 2")
                    continue

                if j_velha[l][c] != " ":
                    print("Erro! espaço já está sendo utilizado.")
                    continue

                j_velha[l][c] = 'O'
                jogadas = jogadas + 1
                jogadores = 2
                break
            except ValueError:
                print("Por favor, insira um número de 0 a 1.")

def vitoria():
    x_ou_o = ['X', 'O']
    
    for i in x_ou_o:
        for l in range(3):
            if j_velha[l][0] == j_velha[l][1] == j_velha[l][2] == i:
                return i
            
        for c in range(3):
            if j_velha[0][c] == j_velha[1][c] == j_velha[2][c] == i:
                return i

        if j_velha[0][0] == j_velha[1][1] == j_velha[2][2] == i or j_velha[0][2] == j_velha[1][1] == j_velha[2][0] == i:
            return i

    return "nao"

while True:
    corpo()
    
    
    jogador1()
    vencedor = vitoria()
    if vencedor != "nao":
        corpo()
        print(f"Jogador (X) venceu")
        break
    
    if jogadas >= max_jogadas:
        corpo()
        print("Empate!")
        break

    corpo()
    jogador2()
    vencedor = vitoria()
    if vencedor != "nao":
        corpo()
        print(f"Jogador (O) venceu")
        break

    if jogadas >= max_jogadas:
        corpo()
        print("Empate")
        break
