# GLOBAL VARIABLES


board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

move = 1
runGame = True
player1won = False
player2won = False
match_tied = False


# FUNCTIONS


def player1turn():
    p1 = int(input("\nPlayer 1: Select [0-8] "))
    if p1 < 0 or p1 > 8:
        print("Invalid Move")
        player1turn()
    row = p1 // 3
    col = p1 % 3
    if board[row][col] == 0:
        board[row][col] = 1
    else:
        print("Invalid Move")
        player1turn()


def player2turn():
    p2 = int(input("\nPlayer 2: Select [0-8] "))
    if p2 < 0 or p2 > 8:
        print("Invalid Move")
        player2turn()
    row = p2 // 3
    col = p2 % 3
    if board[row][col] == 0:
        board[row][col] = 2
    else:
        print("Invalid Move")
        player2turn()


def check_game():
    global player1won
    global player2won

    # Cases where Player 1 wins
    # 0
    if board[0][0] == 1:
        # 012
        if board[0][1] == 1:
            if board[0][2] == 1:
                player1won = True
        # 047
        if board[1][1] == 1:
            if board[2][2] == 1:
                player1won = True
        # 036
        if board[1][0] == 1:
            if board[2][0] == 1:
                player1won = True
    # 1
    if board[0][1] == 1:
        # 147
        if board[1][1] == 1:
            if board[2][1] == 1:
                player1won = True
    # 2
    if board[0][2] == 1:
        # 258
        if board[1][2] == 1:
            if board[2][2] == 1:
                player1won = True
    # 3
    if board[1][0] == 1:
        # 345
        if board[1][1] == 1:
            if board[1][2] == 1:
                player1won = True
    # 6
    if board[2][0] == 1:
        # 678
        if board[2][1] == 1:
            if board[2][2] == 1:
                player1won = True
        # 246
        if board[1][1] == 1:
            if board[0][2] == 1:
                player1won = True

    # Cases where Player 2 wins
    # 0
    if board[0][0] == 2:
        # 012
        if board[0][1] == 2:
            if board[0][2] == 2:
                player2won = True
        # 047
        if board[1][1] == 2:
            if board[2][2] == 2:
                player2won = True
        # 036
        if board[1][0] == 2:
            if board[2][0] == 2:
                player2won = True
    # 1
    if board[0][1] == 2:
        # 147
        if board[1][1] == 2:
            if board[2][1] == 2:
                player2won = True
    # 2
    if board[0][2] == 2:
        # 258
        if board[1][2] == 2:
            if board[2][2] == 2:
                player2won = True
    # 3
    if board[1][0] == 2:
        # 345
        if board[1][1] == 2:
            if board[1][2] == 2:
                player2won = True
    # 6
    if board[2][0] == 2:
        # 678
        if board[2][1] == 2:
            if board[2][2] == 2:
                player2won = True
        # 246
        if board[1][1] == 2:
            if board[0][2] == 2:
                player2won = True


def is_match_tied():
    if not player1won and not player2won:
        no_of_zero = count_zero()
        if no_of_zero == 0:
            return True


def show_board():
    for i in board:
        print(i)


def reset_board():
    global board
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def count_zero():
    count = 0
    for i in board:
        for x in i:
            if x == 0:
                count += 1
    return count


def main():
    print("\n***** TIC TAC TOE *****\n")
    global move
    global runGame
    show_board()
    print("\n1 = Player 1")
    print("2 = Player 2\n")

    while runGame:
        if move % 2 == 1:
            player1turn()
        else:
            player2turn()
        move += 1
        show_board()
        check_game()

        if player1won:
            print("\n*****\nPlayer 1 WON\n*****\n")
        elif player2won:
            print("\n*****\nPlayer 2 WON\n*****\n")
        elif is_match_tied():
            print("\n*****\nMATCH TIED\n*****\n")
        else:
            continue

        if player1won or player1won or is_match_tied():
            print("THANK YOU FOR PLAYING")
            print("Wanna play again?")
            q = input("[ y for yes/ n for no ]")
            if q == 'n':
                runGame = False
            elif q == 'y':
                reset_board()
                main()
            else:
                print("Invalid Input: Quitting Game")


# GAME STARTS


main()
