import json as js
import matplotlib.pyplot as plt
import numpy as np


def average(lst):
    return sum(lst)/len(lst)


results = js.load(open('results.json', mode='r'))
Bn = results[0]
Un = results[1]
Ln = results[2]
Dn = results[3]
Cn = results[4]
Dn_Cn = results[5]
mean_list = [[0 for _ in range(100)] for _ in range(6)]  # Tu przechowujemy średnie Bn, Un, ...

for i in range(6):
    for j in range(100):
        mean_list[i][j] = average(results[i][j])

fig, axes = plt.subplots(3, 6)
t = np.array([[(i+1) * 1000, Bn[i][j]] for j in range(50) for i in range(100)])
x, y = t.T
plt.scatter(x, y, c='red', label='Simulated values')
plt.plot([n for n in range(1000, 100001, 1000)], mean_list[0], 'ko', label='Average')
plt.xlabel("Number of urns")
plt.ylabel("Bn value")
plt.legend()
plt.show()
