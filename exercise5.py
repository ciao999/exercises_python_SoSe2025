import matplotlib.pyplot as plt

#formel für geometrische Reihe ar^n
a = 1
r = -1
n = 100

s_n = []

summe = 0
for k in range(0, n+1):
    summe += a*r**k
    s_n.append(summe)
    
plt.plot(s_n)




