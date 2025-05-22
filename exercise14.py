import numpy as np

y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

mittelwert = np.mean(y)
print(mittelwert)

abw = y -mittelwert


quad_abw = abw**2

sum_quad_abw = np.sum(quad_abw)

varianz = 1 / len(y) * sum_quad_abw

std = np.sqrt(varianz)

print(std)

print(np.std(y))
