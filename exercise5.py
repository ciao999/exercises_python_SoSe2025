import matplotlib.pyplot as plt

#formel für geometrische Reihe ar^n
a = 1
r = 0.5
n = 10

s_n = []

summe = 0
for k in range(n):
    summe += a*r**k
    s_n.append(summe)
    
plt.plot(s_n)
    