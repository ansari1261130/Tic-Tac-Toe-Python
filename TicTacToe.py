import tkinter as tk
from tkinter import messagebox

def printBoard(gameValues):
    # Update the buttons with the current game values
    for i in range(9):
        buttons[i].config(text=gameValues[i])

def checkWin(gameValues):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for win in wins:
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X':
            return 1
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O':
            return 0
    if all(isinstance(item, str) for item in gameValues):
        return -2
    return -1

def buttonClick(index):
    global chance
    if gameValues[index] not in ['X', 'O']:
        gameValues[index] = 'X' if chance == 1 else 'O'
        printBoard(gameValues)
        cwin = checkWin(gameValues)
        if cwin != -1:
            if cwin == 1:
                messagebox.showinfo("Game Over", "Player X Won the match")
            elif cwin == 0:
                messagebox.showinfo("Game Over", "Player O Won the match")
            elif cwin == -2:
                messagebox.showinfo("Game Over", "Game Draw")
            resetGame()
        chance = 1 - chance

def resetGame():
    global gameValues, chance
    gameValues = list(range(9))
    chance = 1
    printBoard(gameValues)

if __name__ == '__main__':
    gameValues = list(range(9))
    chance = 1

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = []
    for i in range(9):
        button = tk.Button(root, text=str(gameValues[i]), font=('normal', 20), height=3, width=6,
                           command=lambda i=i: buttonClick(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

    reset_button = tk.Button(root, text="Reset", font=('normal', 20), height=1, width=6, command=resetGame)
    reset_button.grid(row=3, column=1)

    printBoard(gameValues)
    root.mainloop()
