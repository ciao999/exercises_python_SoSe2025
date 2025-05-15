def buchstaben_zählen(x):
    x_list = list(x)
    x_buch = []
    
    for b in x_list:
        if b.isalpha():
            x_buch.append(b)
    
    return len(x_buch)
    
print(buchstaben_zählen("HWR Berlin 2025"))

#print(buchstaben_zählen("HWR Berlin 2025"))

