a = 1
r = 0.5
s = 0
k = 0

while True:
    summand = a * r**k
    s += summand
    k += 1 
    print(s, end = " ")
        
    if summand < 0.0001:
        break





import matplotlib.pyplot as plt

#geometrische Reihe ar^k
a = 1 #Anfangswert
r = 0.5 #Verhältnis - Wachstumsrate/ratio
s = 0 #aktuelle Summe - was aufsummiert wird
k = 0 #Index oder Laufvariable - zähler für Gliednummer 0, 1, 2...
epsilon = 0.0001

werte = []
schritte = []

while True:
    summand = a * r**k #Variable zum speichern der aktuellen Glieder
    s += summand #jede Runde wird ein Term hinzugefügt
    werte.append(s)
    schritte.append(k)
    k += 1 #Index jede Runde ein neuer
    print(s, end = " ") #ausgabe von s, nebeneinander mit Leerzeile
    
    if summand < epsilon: #break Anweisung wenn summand zu klein wird 
        break
    
plt.plot(schritte, werte, marker='o')
plt.xlabel("Schritte k")
plt.ylabel("Summe s")
plt.grid(True)
plt.show()