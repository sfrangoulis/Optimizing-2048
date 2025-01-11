#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:12:50 2024

@author: stamatisfrangoulis
"""

import tkinter as tk
from tkinter import messagebox
from Game2048 import Game2048  

class Game2048Player:
    def __init__(self):
        self.game = Game2048()
        self.root = tk.Tk()
        self.root.title("2048")
        self.root.geometry("400x400")
        self.root.resizable(True, True)


        self.panel = tk.Frame(self.root)
        self.panel.grid(row=0, column=0, padx=5, pady=5)
        self.tiles = [[tk.Label(self.panel, text="", width=8, height=4, borderwidth=1, relief="solid", font=("Arial", 16))
                       for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                self.tiles[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.refresh_board()

     
        self.root.bind("<KeyPress>", self.key_pressed)


        self.root.mainloop()

    def key_pressed(self, event):
        key = event.char.lower()
        if key in ['w', 'a', 's', 'd']:
            self.game.move(key)
            self.refresh_board()
            if self.game.is_game_over():
                messagebox.showinfo("Game Over", f"Game Over! Score: {self.game.high_score()}")

    def refresh_board(self):
        for i in range(4):
            for j in range(4):
                value = self.game.board[i][j]
                self.tiles[i][j].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {
            0: "#CDC1B4", 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179", 16: "#F59563",
            32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72", 256: "#EDCC61",
            512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"
        }
        return colors.get(value, "#3C3A32")  # Default color for higher numbers

if __name__ == "__main__":
    Game2048Player()