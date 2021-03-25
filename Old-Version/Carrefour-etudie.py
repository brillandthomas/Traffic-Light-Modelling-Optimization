# coding: utf-8s

""" Les variables utiles pour faire les simulations et les optimisations du carrefour étudié """



#Matrice des compatibilités du carrefour : Plusieurs versions sont possibles, notamment si l'on décide de prendre en compte les passages piétons
#Ici on prend les compatibilités correspondant au plan de feux déjà en place, plus les compatibilités évidentes

matrice = [[1,1,0,0,1,0,0,0,1,1,1,0],
           [1,1,0,0,0,0,1,0,0,1,1,1],
           [0,0,1,1,0,1,0,1,1,0,1,1],
           [0,0,1,1,0,1,0,1,1,1,0,1],
           [1,0,0,0,1,0,1,0,1,1,0,1],
           [0,0,1,1,0,1,0,1,1,1,1,1],
           [0,1,0,0,1,0,1,0,1,0,1,1],
           [0,0,1,1,0,1,0,1,1,1,1,0],
           [1,0,1,1,1,0,1,1,1,1,1,1],
           [1,1,0,1,1,1,0,1,1,1,1,1],
           [1,1,1,0,0,0,1,1,1,1,1,1],
           [0,1,1,1,1,1,1,0,1,1,1,1]]

#La liste des phases possibles, qu'on émonde en ne prenant que les phases "maximum"
liste = liste_phases(matrice)
optimise(liste)
    
#Le temps minimal que peut durer une phase dans un plan de feux lors de l'optimisation
tmin = 10

#Le plan de feux mesuré du carrefour étudié
plan = ([([1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],25),([1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],10),([0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],15),([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],25)],75)

#Les propriétés du carrefour étudié, fréquences d'arrivée et vitesse de départ des voitures pour chaque flux (on prend le nombre moyen de voitures mesuré, qu'on divise par la durée du cycle pour la fréquence d'arrivée, pour la fréquence de départ, cela dépend du nombre de voix concernées + ligne droite ou virage + si il y a croisement avec un autre flux, qui ralentit la circulation (par exemple 6 et 8 se croisent)

carrefour = [(9.54/75,1),(9.85/75,1),(4.86/75,0.9),(3.68/75,0.8),(6.97/75,0.7),(0.46/75,0.6),(3.07/75,0.5),(1.07/75,0.5),(7.5/75,0.75),(3.03/75,0.5),(1.56/75,0.5),(0.48/75,0.4)]









"""Un test intéressant serait de tenter d'optimiser un plan tout à fait différent du plan existant, et regarder si l'on arrive à un résultat proche du plan existant
    On construit un plan cohérent mais très mal optimisé, avec de nombreuses phases"""

plan_test = ([],75)
for i in range(7):
    if i == 1:
        plan_test[0].append((12*[0],15))
    else:
        plan_test[0].append((12*[0],10))

plan_test[0][0][0][0] += 1
plan_test[0][0][0][1] += 1
plan_test[0][1][0][2] += 1
plan_test[0][1][0][3] += 1
plan_test[0][2][0][4] += 1
plan_test[0][2][0][5] += 1
plan_test[0][3][0][6] += 1
plan_test[0][4][0][7] += 1
plan_test[0][5][0][8] += 1
plan_test[0][5][0][11] += 1
plan_test[0][6][0][9] += 1
plan_test[0][6][0][10] += 1


    

