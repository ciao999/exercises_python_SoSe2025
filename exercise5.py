import matplotlib.pyplot as plt

#Parameter
a = 1
r = 0.5
n = 10

#leere Liste
s_n = []

#Summe Schritt für Schritt berechnen 
summe = 0 
for k in range(n):
    summe += a * r**k
    s_n.append(summe)
    
#Plot der Werte
plt.plot(s_n, marker="o")
plt.title("Geometrische Reihe a=1, r=0.5")
plt.xlabel("Anzahl Terme n")
plt.ylabel("Summe s_n")
plt.grid(True)

