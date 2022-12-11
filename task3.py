board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

i = 1


def Print(board):
    return ('\n'.join(str(i) for i in board))


def TicTacToeInput(board, i):
    if any(0 in s for s in board):
        if i % 2 != 0:
            Player = "X"
        else:
            Player = "O"

        print("\n Игрок ", Player, " Твой ход!!! \n")
        row = int(input("ВВеди строку (1-3): ")) - 1
        col = int(input("Введи столбец (1-3): ")) - 1
        if board[row][col] == 0:
            board[row][col] = Player
            i += 1
            print(Print(board))
            TicTacToeInput(board, i)
        else:
            print("Что-то не так")
            TicTacToeInput(board, i)


if __name__ == "__main__":
    print("Крестики нолики")
TicTacToeInput(board, i)