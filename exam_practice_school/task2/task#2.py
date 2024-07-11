for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or (not z)) == False:
                    print(w, x, y, z)

                    
