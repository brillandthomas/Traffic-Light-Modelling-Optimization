# coding: utf-8

# plan = couple (liste(phases);durée cycle)
# phase = couple (liste(feux allumés);durée phase)
# carrefour = liste de couples : fréquence entrée, fréquence sortie

""" L'algorithme permettant de simuler l'évolution des voitures  dans le carrefour en fonction d'un plan de feux donnés,
    calculant notamment le temps d'attente total des voitures """



"""
-Approximation = On prend une moyenne du nombre de voitures, à l'aide des mesures effectuées, même si en pratique le nombre est plus fluctuant, il ne serait pas convenable de faire des simulations aléatoires dans le cadre d'optimisation
"""



""" Premier essai de l'algorithme de simulation, pas convenable car le nombre de voitures qui arrive varie en fonction du plan de feux 
def simulation1(carrefour,plan,C):
    attente = 0                                     #temps total d'attente
    temps = 0                                       #temps écoule depuis le début de la simulation
    entrees = 0                                     #nb de voitures entrées
    sorties = 0                                     #nb de voitures sorties
    arrivees_voiture = []                           #liste des voitures, on la construit au fur et à mesure, contient le temps d'arrivée de chacune
    nb_phases = len(plan[0])                        
    nb_flux = len(carrefour)
    files = []
    for i in range(nb_flux):                        #on construit les files d'attente de chaque flux
        files.append([])
    for c in range(C):                              #Pour chaque cycle
        for k in range(nb_phases):                  #Pour chaque phase
            T = plan[0][k][1]                       #Durée de la phase
            for i in range(nb_flux):
                freq_entree = carrefour[i][0]
                freq_sortie = carrefour[i][1]
                for j in range(1,int(freq_entree*T)):                 #Pour chaque voiture entrant durant un cycle
                    files[i].append(entrees)
                    entrees += 1                                     #On la met dans la file du flux correspondant
                    arrivees_voiture.append(temps+(j//freq_entree))  #On stocke la date d'arrivée
                if plan[0][k][0][i] == 1:                            #Si le feu est vert
                    for j in range(int(freq_sortie*T)):
                        if files[i] != []:                           #Tant qu'il reste des voitures en attente
                            v = files[i].pop(0)
                            t = arrivees_voiture[v]
                            sorties += 1
                            dt = temps + (j//freq_sortie) - t        #On calcule le temps d'attente de la voiture étudiée
                            attente += dt
            temps += T
    return(attente,entrees,sorties)
"""
    
  
  
                    
""" Second essai de l'algorithme de simulation """

     
def simulation(carrefour,plan,C):
    attente = 0                                     #temps total d'attente
    temps = 0                                       #temps écoule depuis le début de la simulation
    entrees = 0                                     #nb de voitures entrées
    sorties = 0                                     #nb de voitures sorties
    arrivees_voiture = []                           #liste des voitures, on la construit au fur et à mesure, contient le temps d'arrivée de chacune
    nb_phases = len(plan[0])                        
    nb_flux = len(carrefour)
    files = []
    T = plan[1]
    for i in range(nb_flux):                        #on construit les files d'attente de chaque flux + on fait arriver les voitures
        files.append([])
    for i in range(nb_flux):
        freq_entree = carrefour[i][0]
        for j in range(1,int(freq_entree*C*T)):
            files[i].append(entrees)
            entrees += 1
            arrivees_voiture.append(j//freq_entree)
    for c in range(C):                              #on fait partir les voitures arrivées en fonction du plan de feux
        for k in range(nb_phases):
            T = plan[0][k][1]
            for i in range(nb_flux):
                if plan[0][k][0][i] == 1:
                    freq_sortie = carrefour[i][1]
                    for j in range(1,int(freq_sortie*T)):
                        if files[i] != []:                           
                            t = arrivees_voiture[files[i][0]]
                            dt = temps + (j//freq_sortie) - t       
                            if dt > 0:
                                v = files[i].pop(0)
                                sorties += 1
                                attente += dt
            temps += T               
    return(attente,entrees,sorties)
                

"""
Avantages :
    -Simple à implémenter et à comprendre
    -Fonctionne dans le cas général
    -Rend assez bien compte du comportement des voitures dans le carrefour sur une longue période
    -Complexité en O(entrees + sorties), tout à fait raisonnable
Limites de cet algorithme : 
    Ne rend pas compte des passages au vert, du temps de réaction + de démarrage des conducteurs qui sont plus lents au début de la phase
"""








"""Idée : rajouter une fonction attentes moyennes qui renvoie le tableau des temps d'attente moyens pour chaque flux, afin de voir si l'un des flux est désavantagé.
C'est la même fonction que la simulation, on rajoute simplement une liste qu'on met a jour tout le long """

def attentes(carrefour,plan,C):
    attente = 0
    entrees = 0
    sorties = 0
    temps = 0
    arrivees_voitures = []
    files = []
    Tt = plan[1]
    nb_phases = len(plan[0])
    nb_flux = len(carrefour)
    att = nb_flux*[0]
    nb = nb_flux*[0]
    for i in range(nb_flux):   
        files.append([])
        freq_entree = carrefour[i][0]
        for j in range(1,int(freq_entree*C*Tt)):
            files[i].append(entrees)
            entrees += 1
            arrivees_voitures.append(j//freq_entree)
        nb[i] += len(files[i])
    for c in range(C):
        for k in range(nb_phases):
            phase = plan[0][k]
            T = phase[1]
            for i in range(nb_flux):
                if phase[0][i] == 1:
                    freq_sortie = carrefour[i][1]
                    t1 = 0
                    if plan[0][(k-1)%nb_phases][0][i] == 0:                #On regarde si le feu était au rouge lors de la phase précédente
                        t1 += 4
                    for j in range(1,int(freq_sortie*(T-t1))):
                        if files[i] != []:
                            t = arrivees_voitures[files[i][0]]
                            dt = temps + t1 + (j//freq_sortie) - t       
                            if dt > 0:
                                v = files[i].pop(0)
                                sorties += 1
                                attente += dt
                                att[i] += dt/nb[i]
            temps += T+1
    return(att,attente)