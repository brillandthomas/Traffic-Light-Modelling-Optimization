# coding: utf-8

"""             Fonctions auxiliaires utiles aux fonctions de modification des plans de feux pour l'optimisation        """

#Version simple du score : le temps d'attente des voitures, auquel on ajout le temps d'attente potentiel des voitures encore bloquées au feu
def score(T,ve,vs):
    dv = ve-vs
    Tm = T/vs
    return(int(T+dv*Tm))


#Fonction auxiliaire pour construire la liste des phases possibles
def present(phase,liste):                                           
    n = len(liste)
    m = len(phase)
    ok = False
    i = 0
    while i < n and not ok:
        ok = (phase == liste[i])
        i+=1
    return(ok)




#Construit la liste de toutes les phases possibles
def liste_phases(matrice):
    n = len(matrice)
    liste = [] 
    for i in range(n):
        for j in range(i+1,n):
            if matrice[i][j] == 1:
                file = [i,j]
                phase = n*[0]
                phase[i] += 1
                phase[j] += 1   
                if j+1 == n:
                    liste.append(phase)                 
                for k in range(j+1,n):
                    ok = True
                    for l in file:
                        if matrice[k][l] != 1:
                            ok = False
                    if ok:
                        phase[k] += 1
                    if not present(phase,liste):
                        liste.append(phase)
    return(liste)
            
    
#Fonction auxiliaire utile à "optimise", compare deux phases et renvoie true si phase1 est incluse dans phase2
def inclus(phase1,phase2):
    n = len(phase1)
    ok = True
    i = 0
    while i < n and ok:
        if phase1[i] == 1 and phase2[i] == 0:
            ok = False
        i += 1
    return(ok)
    
    

#"Epure" la liste des phases possibles en ne conservant que les phases ayant le maximum de feux au vert
def optimise(liste):
    n = len(liste)
    i = 0
    while i < n-1:
        j = i+1
        while j < n:
            if inclus(liste[i],liste[j]):
                p = liste.pop(i)
                n -=1
            elif inclus(liste[j],liste[i]):
                p = liste.pop(j)
                n -= 1
            j+=1
        i+=1
    return()
    
    
    


#Vérifie si un feu est au vert dans deux phases du plan de feux
def apparait2fois(plan,i):
    P = len(plan[0])
    ok = 0
    k = 0
    while ok < 2 and k < P:
        if plan[0][k][0][i] == 1:
            ok += 1
        k += 1
    return(ok >= 2)
    
    
#Renvoie la liste des feux au vert dans phase1 et au rouge dans phase2
def feux_menaces(phase1,phase2):
    n = len(phase1)
    liste = []
    for i in range(n):
        if phase1[i] == 1 and phase2[i] == 0:
            liste.append(i)
    return(liste)




"""     Fonctions de modification de plan de feux, utile à l'algorithme d'optimisation, renvoient un nouveau plan donc ne modifient pas en place"""


#Echange les places de deux phases dans le plan de feux
def change_places(plan,k,j):
    nouveau_plan = list(plan[0])
    aux = nouveau_plan[k]
    nouveau_plan[k],nouveau_plan[j] = nouveau_plan[j],aux
    return(nouveau_plan,plan[1])
    
    
#Ajoute dt à la phase k et retire dt a la phase j (en pratique ce sera toujours 5 secondes)
def change_duree(plan,dt,k,j,tmin):
    if plan[0][j][1] - dt < tmin:
        return plan
    else:
        nouveau_plan = list(plan[0])
        nouveau_plan[k] = (nouveau_plan[k][0],nouveau_plan[k][1]+dt)
        nouveau_plan[j] = (nouveau_plan[j][0],nouveau_plan[j][1]-dt)
        return(nouveau_plan,plan[1])
        


#Supprime une phase, si et seulement si tous les feux présents dans la phase apparaissent deux fois
def supprime_phase(plan,k):
    n = len(plan[0][k][0])
    ok = True
    i = 0
    while i < n and ok:
        if plan[0][k][0][i] == 1:
            ok = apparait2fois(plan,i)
        i += 1
    if ok:
        nouveau_plan = list(plan[0])
        dt = nouveau_plan.pop(k)[1]
        if k == n:
            nouveau_plan[0] = (nouveau_plan[0][0],nouveau_plan[0][1] + dt) 
        else:
            nouveau_plan[k-1] = (nouveau_plan[k-1][0],nouveau_plan[k-1][1] + dt)
        return(nouveau_plan,plan[1])
    else:
        return(plan)
       

#Echange la phase k du plan de feux, avec la phase j de la liste des phases de la matrice
def change_phase(plan,k,liste,j):
    nouveau_plan = list(plan[0])
    nouvelle_phase = liste[j]
    if nouveau_plan[k][0] == liste[j]:      
        if j == len(liste)-1:
            nouvelle_phase = liste[0]
        else:
            nouvelle_phase = liste[j+1]
    liste = feux_menaces(nouveau_plan[k][0],nouvelle_phase) 
    for i in liste:                        
        if not apparait2fois(plan,i):     
            return(plan)
    nouveau_plan[k] = (nouvelle_phase,nouveau_plan[k][1])
    return(nouveau_plan,plan[1])
    
        
    


    
    



