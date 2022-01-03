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

fig, (ax1, ax2) = plt.subplots(2, constrained_layout=True, figsize=(15, 6))
# Wykres Un i u(n)
t = np.array([[(i+1) * 1000, Un[i][j]] for j in range(50) for i in range(100)])
x, y = t.T
ax1.scatter(x, y, c='red', label='Simulated values')
ax1.plot([n for n in range(1000, 100001, 1000)], mean_list[1], 'ko', label='Average')
ax1.set_xlabel("Number of urns")
ax1.set_ylabel("Un value")
ax1.set_title("Un and u(n) plot")
ax1.legend()

# Wykres u(n)/n
ax2.plot([(n+1)*1000 for n in range(100)], [mean_list[1][n]/((n+1)*1000) for n in range(100)], 'k', label='u(n)/n')
ax2.set_xlabel("Number of urns")
ax2.set_title("u(n)/n plot")
ax2.set_ylim(0.35, 0.4)
ax2.legend()
plt.savefig("Un_plot.png", bbox_inches='tight')
plt.show()
