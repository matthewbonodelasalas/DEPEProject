import tkinter as tk
import random
from tkinter import messagebox
import time

# Creating Class memory Tile
class MemoryTile:
    def __init__(self, parent):
        self.parent = parent
        self.buttons = [[tk.Button(root,
                                   width=4,
                                   height=2,
                                   command=lambda row=row, column=column: self.choose_tile(row, column)
                                   ) for column in range(4)] for row in range(4)]
        for row in range(4):  # sets the range
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.draw_board()

    # function for the board to show
    def draw_board(self):
        self.answer = list('AABBCCDDEEFFGGHH')  # list of answers
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)
        self.start_time = time.monotonic()  # starts the timer if the program initiates

    # simulation of the tile if the player clicks the tile
    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
        else:
            a, b = self.first
            if self.answer[row][column] == self.answer[a][b]:
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Success!', message='You win! Time: {:.1f}'.format(duration))
                    self.parent.after(5000, self.draw_board)
            else:
                self.parent.after(3000, self.hide_tiles, row, column, a, b)
            self.first = None

    # hides the tiles if the input does not match
    def hide_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', state=tk.NORMAL)

# Main Program to execute

root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()