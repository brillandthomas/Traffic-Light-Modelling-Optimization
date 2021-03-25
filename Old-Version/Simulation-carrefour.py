#coding: utf-8

""" Simulation plus spécifique au carrefour, et plus précise en général
    On met un temps de réaction de 4 secondes lorsque le feu était rouge puis passe au vert
    On rajoute 1 seconde à la fin de chaque phase pour le temps de transition  
    On rajoute des pénalités pour les flux qui se croisent :
        -Si 7 et 3 sont au vert en même temps, 3 est prioritaire sur 7 => on réduit la fréquence de départ (divisée par 2)
        -Si 8 et 4/7 sont au vert en même temps, 4 et 7 sont prioritaires sur 8 => on diminue la fréquence de départ (divisée par 2 ou 4)"""

def simulation(carrefour,plan,C):
    attente = 0
    entrees = 0
    sorties = 0
    temps = 0
    arrivees_voitures = []
    files = []
    Tt = plan[1]
    nb_phases = len(plan[0])
    for i in range(12):   
        files.append([])
        freq_entree = carrefour[i][0]
        for j in range(1,int(freq_entree*C*Tt)):
            files[i].append(entrees)
            entrees += 1
            arrivees_voitures.append(j//freq_entree)
    for c in range(C):
        for k in range(nb_phases):
            phase = plan[0][k]
            T = phase[1]
            for i in range(12):
                if phase[0][i] == 1:
                    freq_sortie = carrefour[i][1]
                    t1 = 0
                    if plan[0][(k-1)%nb_phases][0][i] == 0:                #On regarde si le feu était au rouge lors de la phase précédente
                        t1 += 4
                    if i == 6:
                        if phase[0][3] == 1:
                            freq_sortie = freq_sortie/2
                    if i == 7:
                        if phase[0][3] == 1 or phase[0][6] == 1:
                            freq_sortie = freq_sortie/2
                    for j in range(1,int(freq_sortie*(T-t1))):
                        if files[i] != []:
                            t = arrivees_voitures[files[i][0]]
                            dt = temps + t1 + (j//freq_sortie) - t       
                            if dt > 0:
                                v = files[i].pop(0)
                                sorties += 1
                                attente += dt
            temps += T+1
    return(attente,entrees,sorties)                



def attentes(carrefour,plan,C):
    attente = 0
    att = 12*[0]
    nb = 12*[0]
    entrees = 0
    sorties = 0
    temps = 0
    arrivees_voitures = []
    files = []
    Tt = plan[1]
    nb_phases = len(plan[0])
    for i in range(12):   
        files.append([])
        freq_entree = carrefour[i][0]
        for j in range(1,int(freq_entree*C*Tt)):
            files[i].append(entrees)
            entrees += 1
            arrivees_voitures.append(j//freq_entree)
            nb[i] += 1
    for c in range(C):
        for k in range(nb_phases):
            phase = plan[0][k]
            T = phase[1]
            for i in range(12):
                if phase[0][i] == 1:
                    freq_sortie = carrefour[i][1]
                    t1 = 0
                    if plan[0][(k-1)%nb_phases][0][i] == 0:                #On regarde si le feu était au rouge lors de la phase précédente
                        t1 += 6
                    if i == 6:
                        if phase[0][2] == 1:
                            freq_sortie = freq_sortie/2
                    if i == 7:
                        if phase[0][3] == 1 and phase[0][6] == 1:
                            freq_sortie = freq_sortie/3
                        elif phase[0][3] == 1 or phase[0][6] == 1:
                            freq_sortie = freq_sortie/2
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
    for i in range(12):
        if att[i]-int(att[i]) > 0.5:
            att[i] = int(att[i])+1
        else:
            att[i] = int(att[i])
    return(att,attente)                
