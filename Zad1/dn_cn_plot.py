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
# Wykres Dn-Cn i d(n)-c(n)
t = np.array([[(i+1) * 1000, Dn_Cn[i][j]] for j in range(50) for i in range(100)])
x, y = t.T
ax1.scatter(x, y, c='red', label='Simulated values')
ax1.plot([n for n in range(1000, 100001, 1000)], mean_list[5], 'k', label='Average')
ax1.set_xlabel("Number of urns")
ax1.set_ylabel("Dn-Cn value")
ax1.set_title("Dn-Cn and D(n)-C(n) plot")
ax1.legend()

# Wykres [d(n)-c(n)]/n
ax2.plot([(n+1)*1000 for n in range(100)], [mean_list[5][n]/((n+1)*1000) for n in range(100)], 'k', label='[d(n)-c(n)]/n')
ax2.set_xlabel("Number of urns")
ax2.set_title("[d(n)-c(n)]/n plot")
ax2.legend()

# Wykres d(n)-c(n)/nln(n)
ax3.plot([(n+1)*1000 for n in range(100)], [mean_list[5][n]/((n+1)*1000 * ln((n+1)*1000)) for n in range(100)], 'k', label='[d(n)-c(n)]/n*ln(n)')
ax3.set_xlabel("Number of urns")
ax3.set_title("[d(n)-c(n)]/n*ln(n) plot")
ax3.legend()

# Wykres d(n)-c(n)/n^2
ax4.plot([(n+1)*1000 for n in range(100)], [mean_list[5][n]/(((n+1)*1000) * ln(ln((n+1)*1000))) for n in range(100)], 'k', label='[d(n)-c(n)]/n*ln(ln(n))')
ax4.set_xlabel("Number of urns")
ax4.set_title("[d(n)-c(n)]/n*ln(ln(n)) plot")
ax4.legend()

plt.savefig("Dn_Cn_plot.png", bbox_inches='tight')
plt.show()

