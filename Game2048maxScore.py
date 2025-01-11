from Game2048 import Game2048
import time
import numpy as np
import math

class Game2048maxScore:
    totalTimes=[]

    def maxScore(self, depth=3):
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
        best_score = 0
        best_move = None
        valid_move_found = False

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            if not test_game.is_state_unchanged(game):
                valid_move_found = True
                score = self.evaluate_moves(test_game, depth - 1)
                if score > best_score:
                    best_score = score
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
            return game.high_score()

        moves = ['w', 'a', 's', 'd']
        best_score = float(0)

        for move in moves:
            test_game = Game2048()
            test_game.copy_state()
            test_game.move(move)

            if not test_game.is_state_unchanged(game):
                score = self.evaluate_moves(test_game, depth - 1)
                best_score = max(best_score, score)

        return best_score
    
    def high_score(game):
        return game.high_score
    def meanRunTime(self):
        return np.mean(self.totalTimes)
    
