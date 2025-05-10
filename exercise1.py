def cagr_berechnung(AK, EK, t): #fkt mit 3 Parametern
        AK_abs = abs(AK) #AK und t darf nur positiv sein 
        t_abs = abs(t)  #abs() für absolute Werte ohne Vorzeichen
        cagr = (EK/AK_abs)**(1/t_abs)-1 #Formel nach cagr umgestellt 
        return cagr 
    
cagr = cagr_berechnung(AK = 100,
                       EK = 700,
                       t = 30)

print (100*(1+cagr)**30)
print (120*(1+cagr)**30)
        