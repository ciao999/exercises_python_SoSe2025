def teilbar(x, y):
        if x == y:
            print("x und y sind gleich")
        elif y == 0:
            print("es ist nicht möglich durch 0 zu teilen")
        else:
            if x%y == 0:
                print("x ist durch y teilbar")
            else:
                print("x ist nicht durch y teilbar")
                

teilbar(10,11)
teilbar(5,5)
teilbar(34,0)
teilbar(4,2)

