


tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
win = False
contador = 0

def victory(int):
    print()
    print("player{0} win".format(int), end="\n")
    win = True
    


while win != True:
    

    while True:
        player1 = input("escreva a coordenada da matriz, player1 = 1:\n")
        player1coord = [int(a) for a in str(player1)]
        if player1coord[0] != 0 and player1coord[0] != 1 and player1coord[0] != 2\
        or player1coord[1] != 0 and player1coord[1] != 1 and player1coord[1] != 2:
            print()
            print("Invalid input, try again")
            continue
        if tabuleiro[player1coord[0]][player1coord[1]] == 0:
            tabuleiro[player1coord[0]][player1coord[1]] = 1
            break
        else:
            print("invalid square, try again")
    print()


    for i in range(0,3):
        for j in range(0,3):
            print(f'[{tabuleiro[i][j]}]', end='')
        print()
    
    contador += 1

    if contador > 3:
        if tabuleiro[0][0] == 1 and tabuleiro[0][1] == 1 and tabuleiro[0][2] == 1:
            victory(1)
            break
        if tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][2] == 1:
            victory(1)
            break
        if tabuleiro[0][0] == 1 and tabuleiro[1][0] == 1 and tabuleiro[2][0] == 1:
            victory(1)
            break
        if tabuleiro[1][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[1][2] == 1:
            victory(1)
            break
        if tabuleiro[2][0] == 1 and tabuleiro[2][1] == 1 and tabuleiro[2][2] == 1:
            victory(1)
            break
        if tabuleiro[0][1] == 1 and tabuleiro[1][1] == 1 and tabuleiro[1][2] == 1:
            victory(1)
            break
        if tabuleiro[0][2] == 1 and tabuleiro[1][2] == 1 and tabuleiro[2][2] == 1:
            victory(1)
            break
        if tabuleiro[2][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[0][2] == 1:
            victory(1)
            break

        if contador == 9:
            print()
            print("Empate")
            break
    
    while True:
        player2 = input("escreva a coordenada da matriz, player2 = 2:\n")
        player2coord = [int(a) for a in str(player2)]
        if player1coord[0] != 0 and player1coord[0] != 1 and player1coord[0] != 2\
        or player1coord[1] != 0 and player1coord[1] != 1 and player1coord[1] != 2:
            print()
            print("Invalid input, try again")
            continue
        if tabuleiro[player2coord[0]][player2coord[1]] == 0:
            tabuleiro[player2coord[0]][player2coord[1]] = 2
            break
        else:
            print("invalid square")
        print()

    for i in range(0,3):
        for j in range(0,3):
            print(f'[{tabuleiro[i][j]}]', end='')
        print()

    if contador > 3:
        if tabuleiro[0][0] == 2 and tabuleiro[0][1] == 2 and tabuleiro[0][2] == 2:
            victory(2)
            break
        if tabuleiro[0][0] == 2 and tabuleiro[1][1] == 2 and tabuleiro[2][2] == 2:
            victory(2)
            break
        if tabuleiro[0][0] == 2 and tabuleiro[1][0] == 2 and tabuleiro[2][0] == 2:
            victory(2)
            break
        if tabuleiro[1][0] == 2 and tabuleiro[1][1] == 2 and tabuleiro[1][2] == 2:
            victory(2)
            break
        if tabuleiro[2][0] == 2 and tabuleiro[2][1] == 2 and tabuleiro[2][2] == 2:
            victory(2)
            break
        if tabuleiro[0][1] == 2 and tabuleiro[1][1] == 2 and tabuleiro[1][2] == 2:
            victory(2)
            break
        if tabuleiro[0][2] == 2 and tabuleiro[1][2] == 2 and tabuleiro[2][2] == 2:
            victory(2)
            break
        if tabuleiro[2][0] == 2 and tabuleiro[1][1] == 2 and tabuleiro[1][2] == 2:
            victory(2)
            break

    contador += 1
