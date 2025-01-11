# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Dec 30 18:44:24 2024

# @author: stamatisfrangoulis
# """

# from Game2048 import Game2048
# import time
# import numpy as np


# class Game2048minSquares:
#     totalTimes=[]
#     def minSquares(self,depth=3):
#         game = Game2048()

#         while not game.is_game_over():
#             start_time=time.time()
#             best_move = self.find_best_move_with_fallback(game, depth)
#             end_time=time.time()
#             self.totalTimes.append((end_time-start_time)*1000)
#             game.move(best_move)
#         return game.high_score()
    
#     def find_best_move_with_fallback(self, game, depth):
#         moves = ['w', 'a', 's', 'd']
#         minSum = 16
#         best_move = None
#         valid_move_found = False

#         for move in moves:
#             test_game = Game2048()
#             test_game.copy_state()
#             test_game.move(move)

#             if not test_game.is_state_unchanged(game):
#                 valid_move_found = True
#                 squareSum = self.evaluate_moves(test_game, depth-1)
#                 if squareSum <= minSum:
#                     minSum= squareSum
#                     best_move = move

#         if not valid_move_found:
#             for fallback_move in moves:
#                 test_game = Game2048()
#                 test_game.copy_state()
#                 test_game.move(fallback_move)
#                 if not test_game.is_state_unchanged(game):
#                     return fallback_move

#         return best_move
    
#     def evaluate_moves(self, game, depth):
#         if depth == 0 or game.is_game_over():
#             return game.non_zero_count()

#         moves = ['w', 'a', 's', 'd']
#         minSum = 16

#         for move in moves:
#             test_game = Game2048()
#             test_game.copy_state()
#             test_game.move(move)

#             if not test_game.is_state_unchanged(game):
#                 squareSum = self.evaluate_moves(test_game, depth - 1)
#                 minSum= min(minSum, squareSum)

#         return minSum
    
    

    
#     def high_score(game):
#         return game.high_score
    
#     def meanRunTime(self):
#         return np.mean(self.totalTimes)
from Game2048 import Game2048
import time
import numpy as np
import math

class Game2048minSquares:
    totalTimes=[]

    def minSquares(self, depth=3):
        game = Game2048()

        while not game.is_game_over():
            start_time=time.time()
            best_move = self.find_best_move_with_fallback(game, depth)
            
            end_time=time.time()
            self.totalTimes.append((end_time-start_time)*1000)
            game.move(best_move)

        return game.high_score()

    def find_best_move_with_fallback(self, game, depth):
        moves = ['w', 'a', 's', 'd']
        minSum = 16
        best_move = None
        valid_move_found = False

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            if not test_game.is_state_unchanged(game):
                valid_move_found = True
                squares = self.evaluate_moves(test_game, depth - 1)
                if squares < minSum:
                    minSum = squares
                    best_move = move

        if not valid_move_found:
            for fallback_move in moves:
                test_game = Game2048()
                test_game.copy_state()
                test_game.move(fallback_move)
                if not test_game.is_state_unchanged(game):
                    return fallback_move

        return best_move

    def evaluate_moves(self, game, depth):
        if depth == 0 or game.is_game_over():
            return game.non_zero_count()

        moves = ['w', 'a', 's', 'd']
        minSum = 16

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            if not test_game.is_state_unchanged(game):
                squares = self.evaluate_moves(test_game, depth - 1)
                minSum = min(minSum, squares)

        return minSum
    
    def high_score(game):
        return game.high_score
    def meanRunTime(self):
        return np.mean(self.totalTimes)
    
