#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:50:53 2025

@author: stamatisfrangoulis
"""

import matplotlib.pyplot as plt
import numpy as np
from Game2048stableAlgorithm import Game2048stableAlgorithm


setScores = [0,16,32,64, 128, 256, 512, 1024, 2048, 4096]
setScoresLabels = ["0","16","32","64", "128", "256", "512", "1024", "2048", "4096"]


scores = []
totalTimes=[]
for i in range(100):
    player = Game2048stableAlgorithm()
    scores.append(player.algorithm())
    totalTimes.append(player.meanRunTime())
    


counts = {value: scores.count(value) for value in setScores}


frequencies = list(counts.values())

plt.bar(setScoresLabels, frequencies, color="yellow", edgecolor="black")


plt.xlabel("Score Values")
plt.ylabel("Frequency")
plt.title("Stable Algorithm")
avrgtime=np.mean(totalTimes)
plt.legend([f"Average move runtime: {avrgtime:.4f} ms"])
plt.tight_layout()
plt.show()
