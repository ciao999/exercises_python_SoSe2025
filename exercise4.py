quad_zahl = []

for k in range(1, 11):
    if k % 2 == 0:
        quad_zahl.append(k)
    else:
        quad_zahl.append(k**2)
        
print(quad_zahl)



#Listen-Abstraktion, ohne If-Bedingung
res = [k**2 for k in range(1,11)]
print(res)