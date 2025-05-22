def buchstaben_ändern(string, buchstabe):
    
        string_lower = string.lower()
        
        for v in "aeiou": #insgesamt 5 Runden sind 30 Durchgänge
            
            new_sentence = []
            
            for char in string_lower:
                
                    if char == buchstabe:
                        
                        new_sentence.append(v)
                        
                    else:
                        new_sentence.append(char)
                        
            print("".join(new_sentence)) #Wort wird 5x zsmgebaut 
            
        
buchstaben_ändern(string = "banana",
                          buchstabe = "a") 