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
# Wykres Ln i l(n)
t = np.array([[(i+1) * 1000, Ln[i][j]] for j in range(50) for i in range(100)])
x, y = t.T
ax1.scatter(x, y, c='red', label='Simulated values')
ax1.plot([n for n in range(1000, 100001, 1000)], mean_list[2], 'k', label='Average')
ax1.set_xlabel("Number of urns")
ax1.set_ylabel("Ln value")
ax1.set_title("Ln and l(n) plot")
ax1.legend()

# Wykres l(n)/ln(n)
ax2.plot([(n+1)*1000 for n in range(100)], [mean_list[2][n]/ln((n+1)*1000) for n in range(100)], 'k', label='l(n)/ln(n)')
ax2.set_xlabel("Number of urns")
ax2.set_title("l(n)/ln(n) plot")
ax2.set_ylim(0.5, 0.8)
ax2.legend()

# Wykres l(n)/(ln(n)/(ln(ln(n))))
ax3.plot([(n+1)*1000 for n in range(100)], [mean_list[2][n]/(ln((n+1)*1000)/ln(ln((n+1)*1000))) for n in range(100)], 'k', label='l(n)/(ln(n)/(ln(ln(n))))')
ax3.set_xlabel("Number of urns")
ax3.set_title("l(n)/(ln(n)/(ln(ln(n)))) plot")
ax3.set_ylim(1.5, 1.8)
ax3.legend()

# Wykres l(n)/ln(ln(n))
ax4.plot([(n+1)*1000 for n in range(100)], [mean_list[2][n]/ln(ln(((n+1)*1000))) for n in range(100)], 'k', label='l(n)/ln(ln(n))')
ax4.set_xlabel("Number of urns")
ax4.set_title("l(n)/ln(ln(n)) plot")
ax4.set_ylim(2.8, 3.6)
ax4.legend()
plt.savefig("Ln_plot.png", bbox_inches='tight')
plt.show()
