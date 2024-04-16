import math
import copy

# Retorna a melhor posição que favorece a IA
def get_move(board, ai, me):
    best_score = -(math.inf)
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                tab = copy.deepcopy(board)
                tab[i][j] = ai
                score = minimax(tab, False, ai, me)
                if score > best_score:
                    best_score = score
                    best_move = (i,j)
    
    return best_move

# Implementação do minimax
def minimax(board, maximizing, ai, me):
    win = has_winner(board)

    if has_tie(board):
        return 0
    elif win == ai:
        return 1
    elif win == me:
        return -1

    if maximizing:
        best_score = -(math.inf)
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    tab = copy.deepcopy(board)
                    tab[i][j] = ai
                    score = minimax(tab, False, ai, me)
                    best_score = max((score, best_score))

        return best_score

    else: 
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    tab = copy.deepcopy(board)
                    tab[i][j] = me
                    score = minimax(tab, True, ai, me)
                    best_score = min((score, best_score))

        return best_score

# Checa se existe algum vencedor
def has_winner(table):
    for i in range(3):
        column = list()
        if table[i] == ["X", "X", "X"]:
            return "X"
        elif table[i] == ["O", "O", "O"]:           
            return "O"
        for j in range(3):
            column.append(table[j][i])

        if column == ["X", "X", "X"]:
            return "X"
        elif column == ["O", "O", "O"]:           
            return "O"

    k = 2
    diag_p = list()
    diag_s = list()
    for i in range(3):
        diag_p.append(table[i][i])
        diag_s.append(table[k][i])
        k -= 1

    if diag_p == ["X", "X", "X"]:
        return "X"
    elif diag_p == ["O", "O", "O"]:           
        return "O"
    if diag_s == ["X", "X", "X"]:
        return "X"
    elif diag_s == ["O", "O", "O"]:           
        return "O"

    return False

# Checa se houve impate
def has_tie(table):
    
    if has_winner(table):
        return False

    for i in range(3):
        if " " in table[i]:
            return False

    return True

def print_table(table):
    print("-- -- --")
    for i in range(3):
        print("  ".join(table[i]))
    print("-- -- --")

def game(ai, me):

    table = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
    ]

    running = True
    turn = me

    while running:
        # Vez do jogador
        if turn == me:
            print("\nVez do jogador ")
            linha  = int(input("\nLinha :"))
            coluna = int(input("Coluna:"))

            if table[linha - 1][coluna - 1] == " ":
                table[int(linha - 1)][int(coluna - 1)] = me
                turn = ai

        # Vez da IA
        elif turn == ai:
            cel = get_move(copy.deepcopy(table), ai, me)
            if table[cel[0]][cel[1]] == " ":
                table[cel[0]][cel[1]] = ai
                turn = me

        print_table(table)


        if has_winner(table) == False and has_tie(table) == False:
            continue


        # Executado somente quando existe um vencedor ou houve empate
        if has_winner(table) == "O":
            print("\nA IA venceu!")
        elif has_winner(table) == "X":
            print("\nVocê venceu!")
        else:
            print("\nDeu velha!")

        running = False

game("O", "X")
