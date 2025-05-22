import matplotlib.pyplot as plt

def buchstaben_häufigkeit(x):
    
    mein_d = {} #leeres Dict
    
    x_lower = x.lower()
    
    for b in x_lower:
        
        if b.isalpha(): #nur wenn b alphabetisch ist 
            
            if b in mein_d: #wenn b bereits in der d ist 
            
                mein_d[b] += 1 #füge 1 hinzu
            
            else:
                mein_d [b] = 1 
    
    mein_d_sorted = dict(sorted(mein_d.items())) #dict alphabetisch sortieren
    
    return mein_d_sorted

print(buchstaben_häufigkeit(x = "123banana!!!!"))

plt.bar(bh_dict.keys(), bh_dict.values())