def steigungs_funktion(meine_liste):
        x1 = meine_liste[0]
        y1 = meine_liste[1]
        x2 = meine_liste[2]
        y2 = meine_liste[3]
        
        delta_x = x2 - x1
        delta_y = y2 - y1
        
        if delta_x == 0:
            print("Die Steigung ist nicht definiert")
            
        else:
            steigung = delta_y / delta_x
            return steigung 
        
test_list = [4,2,8,12]
print(steigungs_funktion(test_list))


