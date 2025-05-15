def vokon_zählen(x):
    x_lower = x.lower()
    x_lower_list = list(x_lower)
    vokalen = "aieou"
    
    v = [] # Hier speichern wir Vokale
    k = [] # Hier speichern wir Konsonanten
    
    for b in x_lower_list:
        
        # Hier prüfen wir ob b ein Buchstabe ist
        if b.isalpha(): #Buchstabe?
            k.append(b)
            
        # Hier prüfen wir ob b ein Vokal ist
        if b in vokalen:
            v.append(b)
        
            
    return f"Im String {x} gibt es {len(v)} Vokalen und {len(k)-len(v)} Konsonanten."
     # f" interaktiver String, passt sich an wenn Variablen sich ändenr
     
     
     # return [len(v), len(k)-len(v)]
          
        
print(vokon_zählen("Berlin I love you"))

