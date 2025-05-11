# Neue Funktionen erstellen

def grüße_funktion():
        print("Moin")
        
def abschieds_funktion():
        print("Tschüss")
        
def zusammenfunktion():
        grüße_funktion()
        abschieds_funktion()

zusammenfunktion()



# Fkt die Argument annimmt und Satz zurück gibt (Parameter = Platzhalter)
# Dann Namen als Zeichenkette in Fkt geben (Argument = Wert)


def mein_name(name):
        print("Ich bin " + name)
        
mein_name("Claire")

# Funktionen mit Rückgabewert

def quadrat_fkt(x):
        x_quadrat = x**2  #temporäre Variable - speichert Wert
        return x_quadrat
    
print(quadrat_fkt(2)**2)



# Methode einer Klasse - Unterschied zur FKT existiert innerhalb einer Klasse und bezieht sich auf ein Objekt. 

class Rechner:                  # Klasse ist wie grober Bauplan 
    def addiere(self, a, b):   # addiere() ist Methode der Klasse Rechner
        return a +b 
    
rechner = Rechner()         # Instanziierung der Klasse wird zum Objekt
ergebnis = rechner.addiere(178, 3)  # Methode wird über Objekt abgerufen
print(ergebnis)


# Bedingte Ausführung mit if-Anweisungen 
x = 1

if x > 0:
    print("X ist positiv")
else:
    print("x ist negativ")

# Bei mehr als 2 Möglichkeiten Bedingungen mit elif verketten
x = 0

if x > 0:
    print("X ist positiv")

elif x > 0:
    print("x ist negativ")
    
else:
    print("x ist null")

# Alternativ Bedingungen verschachten
x = 5
y = 4

if x == y:
    print("x und y sind gleich")
else:
    if x < y:
        print("x ist kleiner als y")
    else:
        print("x ist größer als y")

# Verschachtelte Bedingungen vereinfachen 
x = -1
y = -3

if x < 0:
    if y < 0:
        print("x und y sind beide negativ")
        
# Vereinfachen mit and Operator 

if x < 0 and y < 0:
    print("X und y sind beide negativ")

