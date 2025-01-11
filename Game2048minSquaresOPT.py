#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 02:39:58 2025

@author: stamatisfrangoulis
"""

from Game2048 import Game2048
import time
import numpy as np

class Game2048minSquares:
    totalTimes = []
    memo = {}  # Cache for previously computed results

    def minSquares(self, depth=3):
        game = Game2048()

        while not game.is_game_over():
            start_time = time.time()
            best_move = self.find_best_move_with_fallback(game, depth)
            end_time = time.time()
            self.totalTimes.append((end_time - start_time) * 1000)
            game.move(best_move)

        return game.high_score()

    def find_best_move_with_fallback(self, game, depth):
        moves = ['w', 'a', 's', 'd']
        minSquares = 16  # Max grid size (number of non-zero squares)
        best_move = None
        valid_move_found = False

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            # Only evaluate moves that result in a change
            if not test_game.is_state_unchanged(game):
                valid_move_found = True
                squares = self.evaluate_moves(test_game, depth - 1)
                if squares < minSquares:
                    minSquares = squares
                    best_move = move

        # Fallback if no valid move is found
        if not valid_move_found:
            for fallback_move in moves:
                test_game = Game2048()
                test_game.copy_state()
                test_game.move(fallback_move)
                if not test_game.is_state_unchanged(game):
                    return fallback_move

        return best_move

    def evaluate_moves(self, game, depth):
        # Use cached results if available
        game_state = tuple(tuple(row) for row in game.board)  # Convert board to immutable tuple
        if (game_state, depth) in self.memo:
            return self.memo[(game_state, depth)]

        # Base case
        if depth == 0 or game.is_game_over():
            result = game.non_zero_count()
            self.memo[(game_state, depth)] = result  # Cache result
            return result

        moves = ['w', 'a', 's', 'd']
        minSquares = 16  # Max number of non-zero squares in a 4x4 grid

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            # Only evaluate if the state changes
            if not test_game.is_state_unchanged(game):
                squares = self.evaluate_moves(test_game, depth - 1)
                minSquares = min(minSquares, squares)

        self.memo[(game_state, depth)] = minSquares  # Cache the result
        return minSquares

    def high_score(self, game):
        return game.high_score()  # Return high score properly

    def meanRunTime(self):
        return np.mean(self.totalTimes)
