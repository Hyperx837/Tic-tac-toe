from tkinter import messagebox
import tkinter as tk
import numpy as np


def define_sign(idx):
    def set_buttonval(idx):
        index = buttons[idx]
        global player_turn, board, moves, playable
        button = globals()[f'button{idx}']
        def create_label(text): return tk.Label(root, text=text, fg='white',
                                                bg='purple', font='times 15').place(x=150, y=550)
        if (not board[index] == 'X' or board[index] == 'O') and playable:
            turn = player_dict[player_turn]
            button['text'] = turn
            button['bg'] = bgcolor[turn]
            button['fg'] = font_color[turn]
            board[index] = turn
            winner = get_winner(board)
            print(winner)
            if winner:
                globals()['won'] = True
                new_game = messagebox.askquestion('New Game', f'Player {player_turn} won. Do you want a new game?')
                print(new_game)
                if new_game == 'yes':
                    reset()

                # else:
                # tk.Label(popup, text=f'Player {player_turn} won', font='times 15').pack()
                # tk.Button(popup, text='new game', font='times 15', command=lambda: reset()).pack()
                # print('has winner', turn, '\n')
                # globals()['won'] = True
                # create_label(f'player {player_turn} won')

                playable = False

            else:
                player_turn = turn_dict[player_turn]
                # print(index, 'pressed\n')
                print(display_turn.format(player_turn))

            moves += 1
            print(moves)
            # print(board)

        else:
            print('hi not playble\n')

        if moves == 9 and playable:
            playable = False
            create_label(f'draw')

    return lambda: set_buttonval(idx)


def reset():
    global board, moves, playable, player_turn
    board = np.array([['n', 'c', 'm'],
                      ['v', 'l', 't'],
                      ['b', 'g', 'r']])

    moves = 0
    playable = True
    player_turn = '1'
    main(root)


def get_winner(board):
    has_winner = []
    for letter in 'X', 'O':
        has_winner.append(
            (
                map(letter.__eq__, [board[(0, 0)], board[(0, 1)], board[(0, 2)]]),  # horizontal win
                map(letter.__eq__, [board[(1, 0)], board[(1, 1)], board[(1, 2)]]),
                map(letter.__eq__, [board[(2, 0)], board[(2, 1)], board[(2, 2)]]),

                map(letter.__eq__, [board[(0, 0)], board[(1, 0)], board[(2, 0)]]),  # vertical win
                map(letter.__eq__, [board[(0, 1)], board[(1, 1)], board[(2, 1)]]),
                map(letter.__eq__, [board[(0, 2)], board[(1, 2)], board[(2, 2)]]),

                map(letter.__eq__, [board[(0, 0)], board[(1, 1)], board[(2, 2)]]),  # diagonal win
                map(letter.__eq__, [board[(0, 2)], board[(1, 1)], board[(2, 0)]])
            )
        )
        has_winner.append(map(all, has_winner.pop(-1)))

    return any(map(any, has_winner))


def main(root):
    root.title('tic tac toe')
    root.geometry('600x600+100+100')

    for i, letter in zip(range(1, 3), ['X', 'O']):
        tk.Label(root, text=f'Player {i}: {letter}',
                 font='times 15').grid(row=0, column=i)

    idx_column_row = zip(range(1, 10),
                         [1, 2, 3] * 3, [1] * 3 + [4] * 3 + [7] * 3)

    for idx, column, row in idx_column_row:
        globals()[f'button{idx}'] = tk.Button(root, width=20, height=10,
                                              command=define_sign(idx))

        button = globals()[f'button{idx}']
        button.grid(row=row, column=column)

    tk.Button(root, text='reset', font='times 15', command=reset).place(x=500, y=50)
    print('player 1 turn')
    def func():
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', root.destroy)
    root.mainloop()


# nonlocal won
root = tk.Tk()
moves = 0
won = False
playable = True
display_turn = 'player {} turn'
player_turn = '1'
turn_dict = {'2': '1', '1': '2'}
player_dict = {'1': 'X', '2': 'O'}
bgcolor = {'X': 'black', 'O': 'red'}
font_color = {'X': 'white', 'O': 'black'}
rows_columns = zip([0] * 3 + [1] * 3 + [2] * 3,
                   [0, 1, 2] * 3)

buttons = dict(zip(range(1, 10), rows_columns))
board = np.array([['n', 'c', 'm'],
                  ['v', 'l', 't'],
                  ['b', 'g', 'r']])

if __name__ == "__main__":
    main(root)
