#!/user/bin/python3

import os,sys
import numpy as np
import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace('\n','').upper()[0:100000]
window = 1000
at = []
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
    at.append((win.count('A') + win.count('T')) / window)

plt.figure(figsize=(20,10))
plt.plot(at,label="AT_Content")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.legend()

plt.savefig("L16_1.png",transparent=True) 
plt.show()
