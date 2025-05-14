def spar_funktion(AK, SR, i, lz): 
        kapital_entwicklung = []
        kapital = AK
        
        for jahr in range(lz):
            kapital = kapital * (1 + i) + SR
    
        kapital_entwicklung.append(round(kapital,2))

        return kapital_entwicklung

ergebnis = spar_funktion(AK=10000, SR=1000, i=0.01, lz=10)
print(ergebnis)

#Gibt keine Liste aus, sondern nur eien Zahl

