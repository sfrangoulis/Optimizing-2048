#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:35:45 2024

@author: stamatisfrangoulis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:44:24 2024

@author: stamatisfrangoulis
"""

from Game2048 import Game2048
import time
import numpy as np

class Game2048stableAlgorithm:
    totalTimes=[]
    def algorithm(self):
        game = Game2048()

        while not game.is_game_over():
            start_time=time.time()
            best_move = self.find_best_move(game)
            end_time=time.time()
            self.totalTimes.append((end_time-start_time)*1000)
            game.move(best_move)
        return game.high_score()
    
    def find_best_move(self, game):
        if(game.check_move('s')):
            return 's'
        elif(game.check_move('a')):
            return 'a'
        elif(game.check_move('d')):
            return 'd'
        else:
            return 'w'
        
    
    def high_score(game):
        return game.high_score
    
    def meanRunTime(self):
        return np.mean(self.totalTimes)