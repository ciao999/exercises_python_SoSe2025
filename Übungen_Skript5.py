#While Schleifen

k = 3
while k > 0:
    print(k)
    k -= 1
print("Go!")
   

k = 0
while k < 100:
    print(k)
    k += 1
    if k == 5:
        break
    
k = 0
while k < 100:
    print(k, end = " ") #zahlen nebeneinander mit Leerzeichen
    k += 1
    
k = 0
while k < 100:
    print(k) #zahlen untereinander bis 100
    k += 1
    if k == 50:
        break
    

#Strings
    
obst = "Banane"
print(len(obst))

print(obst[0])
print(obst[1:3])

for buchstaben in obst:
    print(buchstaben)


meine_liste = list(obst)
meine_liste[1] = "u"
meine_liste[3] = "u"
meine_liste[5] = "u"

" ".join(meine_liste)
print(meine_liste)

print("Banana".lower())
print("Banana".upper())
print("Banana".replace("a", "u"))
print("Banana".count("a"))


#Exercise7

def buchstaben_fkt(x): #Fkt definieren mit x als Parameter
    x_liste_alles = list(x) #liste anlegen für alle Werte für x - sammelstelle
    buchstaben_liste = [] #leere Liste für Buchstaben in den Werten
    
    for b in x_liste_alles: #jeden Wert aus x-liste mit for-schleife prüfen
        if b.isalpha(): #wenn wert ein Buchstabe ist
            buchstaben_liste.append(x) #dann wird wert buchstaben liste hinten hinzugefügt
    
    return(len(buchstaben_liste)) #fkt gibt länge der buchstaben der Fkt zurück

print(buchstaben_fkt("h28sdfghjk3883dd2")) #fkt aufrufen und buchstaben zählen




#Dictionary

thisdict = {
    "brand" :"BMW",  #Schlüssel und Werte
    "Model" :"3er",
    "Year" : 2023
    }

print(thisdict["Year"])  #Abruf eines Wertes über Schlüssel wie Liste

thisdict["brand"] = "Tesla"  #Überschreiben der Werte
print(thisdict)

thisdict["Portugal"] = "Lissabon" #Neues Paar hinzufügen
print(thisdict)

        
