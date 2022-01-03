import json as js
import matplotlib.pyplot as plt
import numpy as np
from numpy import log as ln


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

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, constrained_layout=True, figsize=(15, 12))
# Wykres Dn i d(n)
t = np.array([[(i+1) * 1000, Dn[i][j]] for j in range(50) for i in range(100)])
x, y = t.T
ax1.scatter(x, y, c='red', label='Simulated values')
ax1.plot([n for n in range(1000, 100001, 1000)], mean_list[3], 'k', label='Average')
ax1.set_xlabel("Number of urns")
ax1.set_ylabel("Dn value")
ax1.set_title("Dn and d(n) plot")
ax1.legend()

# Wykres d(n)/n
ax2.plot([(n+1)*1000 for n in range(100)], [mean_list[3][n]/((n+1)*1000) for n in range(100)], 'k', label='d(n)/n')
ax2.set_xlabel("Number of urns")
ax2.set_title("d(n)/n plot")
ax2.legend()

# Wykres d(n)/n*ln(n)
ax3.plot([(n+1)*1000 for n in range(100)], [mean_list[3][n]/((n+1)*1000 * ln((n+1)*1000)) for n in range(100)], 'k', label='d(n)/n*ln(n)')
ax3.set_xlabel("Number of urns")
ax3.set_title("d(n)/n*ln(n) plot")
ax3.set_ylim(1, 1.5)
ax3.legend()

# Wykres d(n)/n^2
ax4.plot([(n+1)*1000 for n in range(100)], [mean_list[3][n]/(((n+1)*1000) ** 2) for n in range(100)], 'k', label='d(n)/n^2')
ax4.set_xlabel("Number of urns")
ax4.set_title("d(n)/n^2 plot")
ax4.legend()

plt.savefig("Dn_plot.png", bbox_inches='tight')
plt.show()
