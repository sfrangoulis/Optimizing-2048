#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:49:58 2025

@author: stamatisfrangoulis
"""

import matplotlib.pyplot as plt
import numpy as np
from Game2048minSquaresOPT import Game2048minSquares


setScores = [0,16,32,64, 128, 256, 512, 1024, 2048, 4096]
setScoresLabels = ["0","16","32","64", "128", "256", "512", "1024", "2048", "4096"]


scores = []
totalTimes=[]
givenDepth=3
for i in range(100):
    player = Game2048minSquares()
    scores.append(player.minSquares(depth=givenDepth))
    totalTimes.append(player.meanRunTime())
    


counts = {value: scores.count(value) for value in setScores}


frequencies = list(counts.values())

plt.bar(setScoresLabels, frequencies, color="yellow", edgecolor="black")


plt.xlabel("Score Values")
plt.ylabel("Frequency")
plt.title(f"Min Tiles in {givenDepth} moves")
avrgtime=np.mean(totalTimes)
plt.legend([f"Average move runtime: {avrgtime:.4f} ms"])
plt.tight_layout()
plt.show()
