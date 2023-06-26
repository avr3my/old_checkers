from os import system
from time import sleep


def to_string(board, player):

    if player.color == white:
        return ("\n"
                "    1   2   3   4   5   6   7   8\n"
                "  =================================\n"
                f"a | {board['a1']} | ■ | {board['a3']} | ■ | {board['a5']} | ■ | {board['a7']} | ■ | \n"
                "  =================================\n"
                f"b | ■ | {board['b2']} | ■ | {board['b4']} | ■ | {board['b6']} | ■ | {board['b8']} | \n"
                "  =================================\n"
                f"c | {board['c1']} | ■ | {board['c3']} | ■ | {board['c5']} | ■ | {board['c7']} | ■ | \n"
                "  =================================\n"
                f"d | ■ | {board['d2']} | ■ | {board['d4']} | ■ | {board['d6']} | ■ | {board['d8']} | \n"
                "  =================================\n"
                f"e | {board['e1']} | ■ | {board['e3']} | ■ | {board['e5']} | ■ | {board['e7']} | ■ | \n"
                "  =================================\n"
                f"f | ■ | {board['f2']} | ■ | {board['f4']} | ■ | {board['f6']} | ■ | {board['f8']} | \n"
                "  =================================\n"
                f"g | {board['g1']} | ■ | {board['g3']} | ■ | {board['g5']} | ■ | {board['g7']} | ■ | \n"
                "  =================================\n"
                f"h | ■ | {board['h2']} | ■ | {board['h4']} | ■ | {board['h6']} | ■ | {board['h8']} | \n"
                "  =================================\n")
    if player.color == black:
        return ("\n"                         
                "    8   7   6   5   4   3   2   1\n"
                "  =================================\n"
                f"h | {board['h8']} | ■ | {board['h6']} | ■ | {board['h4']} | ■ | {board['h2']} | ■ |  \n"
                "  =================================\n"
                f"g | ■ | {board['g7']} | ■ | {board['g5']} | ■ | {board['g3']} | ■ | {board['g1']} |\n"
                "  =================================\n"
                f"f | {board['f8']} | ■ | {board['f6']} | ■ | {board['f4']} | ■ | {board['f2']} | ■ |  \n"
                "  =================================\n"
                f"e | ■ | {board['e7']} | ■ | {board['e5']} | ■ | {board['e3']} | ■ | {board['e1']} |\n"
                "  =================================\n"
                f"d | {board['d8']} | ■ | {board['d6']} | ■ | {board['d4']} | ■ | {board['d2']} | ■ |  \n"
                "  =================================\n"
                f"c | ■ | {board['c7']} | ■ | {board['c5']} | ■ | {board['c3']} | ■ | {board['c1']} |\n"
                "  =================================\n"
                f"b | {board['b8']} | ■ | {board['b6']} | ■ | {board['b4']} | ■ | {board['b2']} | ■ |  \n"
                "  =================================\n"
                f"a | ■ | {board['a7']} | ■ | {board['a5']} | ■ | {board['a3']} | ■ | {board['a1']} |\n"
                "  =================================\n")


white = chr(9675)
black = chr(9679)

# board = {
#     'b8': black, 'd8': ' ', 'f8': white, 'h8': white,
#     'a7': black, 'c7': black, 'e7': ' ', 'g7': white,
#     'b6': black, 'd6': ' ', 'f6': white, 'h6': white,
#     'a5': black, 'c5': black, 'e5': ' ', 'g5': white,
#     'b4': black, 'd4': ' ', 'f4': white, 'h4': white,
#     'a3': black, 'c3': black, 'e3': ' ', 'g3': white,
#     'b2': black, 'd2': ' ', 'f2': white, 'h2': white,
#     'a1': black, 'c1': black, 'e1': ' ', 'g1': white,
#     'r': ' '
# }


board = {
    'b8': black, 'd8': ' ', 'f8': white, 'h8': white,
    'a7': black, 'c7': black, 'e7': ' ', 'g7': white,
    'b6': black, 'd6': ' ', 'f6': white, 'h6': white,
    'a5': black, 'c5': black, 'e5': white, 'g5': white,
    'b4': black, 'd4': ' ', 'f4': ' ', 'h4': white,
    'a3': black, 'c3': black, 'e3': white, 'g3': white,
    'b2': black, 'd2': black, 'f2': white, 'h2': white,
    'a1': black, 'c1': black, 'e1': ' ', 'g1': white,
    'r': ' ',
}


class players:
    def __init__(self, name, color):
        self.name = name
        self.color = color


player1 = players("Avremy", white)
player2 = players("Mendy", black)


def avail_for_sec_eat(player, move, goto) -> str:
    opos = white
    if player.color == white:
        opos = black

    row1 = ord(move[0]) - 2 == ord(goto[0])
    spot1 = ord(move[1]) + 2 == ord(goto[1])
    position1 = chr(ord(move[0]) - 1) + chr(ord(move[1]) + 1)
    spot2 = ord(move[1]) - 2 == ord(goto[1])
    position2 = chr(ord(move[0]) - 1) + chr(ord(move[1]) - 1)

    row2 = ord(move[0]) + 2 == ord(goto[0])
    spot3 = ord(move[1]) + 2 == ord(goto[1])
    position3 = chr(ord(move[0]) + 1) + chr(ord(move[1]) + 1)
    spot4 = ord(move[1]) - 2 == ord(goto[1])
    position4 = chr(ord(move[0]) + 1) + chr(ord(move[1]) - 1)

    if row1 and spot1 and board[position1] == opos:
        return position1
    if row1 and spot2 and board[position2] == opos:
        return position2
    if row2 and spot3 and board[position3] == opos:
        return position3
    if row2 and spot4 and board[position4] == opos:
        return position4
    return ''


def avail_for_walk(player, move, goto) -> bool:
    if player.color == white:
        row = ord(move[0]) - 1 == ord(goto[0])
    else:
        row = ord(move[0]) + 1 == ord(goto[0])
    spot = ord(move[1]) + 1 == ord(goto[1]) or ord(move[1]) - 1 == ord(goto[1])
    if row and spot:
        return True
    return False


def avail_for_eat(player, move, goto) -> str:
    if player.color == white:
        row = ord(move[0]) - 2 == ord(goto[0])
        spot1 = ord(move[1]) + 2 == ord(goto[1])
        position1 = chr(ord(move[0]) - 1) + chr(ord(move[1]) + 1)
        spot2 = ord(move[1]) - 2 == ord(goto[1])
        position2 = chr(ord(move[0]) - 1) + chr(ord(move[1]) - 1)

        if row and spot1 and board[position1] == black:
            return position1
        if row and spot2 and board[position2] == black:
            return position2
    if player.color == black:
        row = ord(move[0]) + 2 == ord(goto[0])
        spot1 = ord(move[1]) + 2 == ord(goto[1])
        position1 = chr(ord(move[0]) + 1) + chr(ord(move[1]) + 1)
        spot2 = ord(move[1]) - 2 == ord(goto[1])
        position2 = chr(ord(move[0]) + 1) + chr(ord(move[1]) - 1)

        if row and spot1 and board[position1] == white:
            return position1
        if row and spot2 and board[position2] == white:
            return position2
    return ''


def make_move(player):
    system('cls')
    print(to_string(board, player))
    move = input(f"\n{player.name} make a move\n")
    while move not in board or board[move] != player.color:
        move = input("It\'s not your tool, Try again\n")
    goto = input(f"Where do want to move {move}? to restart press 'r'\n")
    while goto not in board or board[goto] != ' ':
        move = input("This spot is not available, Try again\n")
    if goto == 'r':
        return make_move(player)
    walk = avail_for_walk(player, move, goto)
    eat = avail_for_eat(player, move, goto)
    while not walk and not eat:
        print("You can\'t go there")
        move = input(f"\n{player.name} make a move\n")
        while move not in board or board[move] != player.color:
            move = input("It\'s not your tool, Try again\n")
        goto = input(f"Where do want to move {move}? to restart press 'r'\n")
        while goto not in board or board[goto] != ' ':
            move = input("This spot is not available, Try again\n")
        if goto == 'r':
            return make_move(player)
        walk = avail_for_walk(player, move, goto)
        eat = avail_for_eat(player, move, goto)
    if walk:
        board[move] = ' '
        board[goto] = player.color
    if eat:
        board[move] = ' '
        board[eat] = ' '
        board[goto] = player.color
    system('cls')
    print(to_string(board, player))
    sleep(.7)
    while eat:
        move = goto
        goto = input("End your turn (or play second move if available)\n")
        if goto == '':
            break
        eat = avail_for_sec_eat(player, move, goto)
        if eat:
            board[move] = ' '
            board[eat] = ' '
            board[goto] = player.color
            system('cls')
            print(to_string(board, player))
            sleep(.3)
    sleep(1.5)


def make_move2(player):
    global board
    system('cls')
    print(to_string(board, player))
    move = input(f"\n{player.name} make a move\n").split()
    while move[0] not in board or board[move[0]] != player.color:
        move = input("It\'s not your tool, Try again\n").split()
    temp = move.pop(0)
    for i in move:
        if i not in board or board[i] != ' ':
            print("This spot is not available, Try again\n")
            return make_move2(player)
    move.insert(0, temp)
    moves = len(move) - 1
    if abs(ord(move[0][1]) - ord(move[1][1])) == 1:  # checking for walk-ability
        if moves != 1:
            print("Too many arguments were given\n")
            return make_move2(player)
        if not avail_for_walk(player, move[0], move[1]):
            print("Not a legal move, try again\n")
            return make_move2(player)
        board[move[0]] = ' '
        board[move[1]] = player.color
        return
    elif abs(ord(move[0][1]) - ord(move[1][1])) == 2:  # checking for eat-ability
        backup_board = board.copy()
        eat = avail_for_eat(player, move[0], move[1])

        if eat:
            board[move[0]] = ' '
            board[eat] = ' '
            board[move[1]] = player.color
        else:
            print("Not a legal move, Play again")
            return make_move2(player)
        for i in range(1, moves):
            eat = avail_for_sec_eat(player, move[i], move[i + 1])
            if eat:
                board[move[i]] = ' '
                board[eat] = ' '
                board[move[i + 1]] = player.color
            else:
                print("Not a legal move, Play again")
                board = backup_board
                return make_move2(player)
    else:
        print("Not a legal move, Play again")
        return make_move2(player)
    sleep(1.5)


def game_play():
    player1.name = input("Please enter player 1's name\n")
    if input(f"{player1.name}Please choose your color") == 'black':
        player1.color = black
    player2.name = input("Please enter player 2's name\n")
    if player1.color == white:
        player = player2
    else:
        player = player1

    while black in board.values() and white in board.values():
        if player == player1:
            player = player2
        else:
            player = player1
        make_move2(player)
    sleep(1.5)
    system('cls')
    print(player.name, 'won the game!')


game_play()
input()
