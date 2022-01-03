import numpy as np
import json as js


# n — liczba urn / step
# k — krok symulacji
def simulation(n, k, step=1000):
    lista = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(6)]
    generator = np.random.default_rng()
    '''
    // 0 = Bn
    // 1 = Un
    // 2 = Ln
    // 3 = Dn
    // 4 = Cn
    // 5 = Dn - Cn
    '''
    for i in range(1, n+1):
        for j in range(1, k+1):
            urns = [0] * i * step
            ball = 0
            print((((i-1)*50 + j) / 5000) * 100)
            empty = i * step
            at_least_two = 0
            maximum = 0
            while at_least_two < i * step:
                urn_array = generator.integers(low=i * step, size=i*step*100)  # Tak jest szybciej niż losownanie ich po kolei
                for urn in urn_array:
                    ball += 1

                    if lista[0][i-1][j-1] == 0:  # Sprawdzamy, czy mamy już bn
                        if urns[urn] != 0:  # Sprawdzamy, czy w urnie jest już kula
                            lista[0][i-1][j-1] = ball  # Jeżeli tak to zapamiętujemy moment pierwszego zderzenia

                    urns[urn] += 1
                    if urns[urn] > maximum:  # Porównujemy obecne maksimum z potencjalnym i zamieniamy
                        maximum = urns[urn]

                    if lista[4][i-1][j-1] == 0:  # Sprawdzamy, czy mamy już cn
                        if urns[urn] == 1:  # Do urny wleciała nowa kula
                            empty -= 1  # Liczymy ile mamy pustych urn
                        if empty == 0:  # Brak pustych urn
                            lista[4][i-1][j-1] = ball  # Zapamiętujemy moment zapełnienia wszystkich urn

                    if ball == i * step:  # Wrzuciliśmy tyle kul ile jest urn
                        lista[1][i - 1][j - 1] = empty  # Tyle mamy teraz pustych urn
                        lista[2][i - 1][j - 1] = maximum  # Tyle wynosi maksymalna liczba urn

                    if urns[urn] == 2:  # Sprawdzamy, czy mamy 2 kule w urnie
                        at_least_two += 1
                    if at_least_two == i * step:  # W każdej urnie mamy 2 kule
                        lista[3][i-1][j-1] = ball  # Zapamiętujemy moment zapełnienia wszystkich urn co najmniej 2 kulami
                        lista[5][i-1][j-1] = lista[3][i-1][j-1] - lista[4][i-1][j-1]  # Odejmujemy Dc-Cn
                        break
    return lista


if __name__ == '__main__':
    results = simulation(100, 50, step=1000)
    js.dump(results, open('results2.json', mode='w'))
