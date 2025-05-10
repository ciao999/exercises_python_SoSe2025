#Übung Variable pounds = 2.205 erstellen und 
#200 pounds in kg konvertieren (1kg = 2.205)

pounds = 2.205
kg = 200
print(kg)
result = kg/pounds
print(result)


# Variablentyp herausfinden
print(type(kg))

#Berechne Zukunftswert A von 100€ (P) in 10 Jahren (t)
#bei jährlichen Zinssatz i von 3% 

P = 100
t = 10
i = 0.03

A = P * (1 + i)**t
print(A)

#Berechne den Zukunftswert A von 1€ P in einem Jahr t 
#die jede Minute n zu einem jährlichen Zinssatz von 100% verzinst wird 

P = 1
t = 1
i = 1
n = 24*60*365

A = P * (1 + i/n)**(t*n)
print(A)
