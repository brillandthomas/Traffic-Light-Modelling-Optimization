#coding: utf-8
import random
import time

""" Un algorithme naif glouton : On se donne un nombre d'itérations ou un temps de calcul, pour chaque itération on tire un entier entre 1 et 4 
    Selon l'entier tiré, on réalise l'une des 4 modifications de plan programmées dans "auxiliaire.py", en choisissant aléatoirement les phases concernées. Si le score du nouveau plan obtenu est meilleur, on choisit ce plan, et on continue.
    Avantages :
        - Simple à programmer
        - Simple à modifier, on peut facilement rajouter une modification possible
        -Peut renvoyer une meilleure solution rapidement, même si elle n'est pas optimale
    Inconvénients :
        - Inconvénient majeur : Si on prend la mauvaise direction pour l'optimisation, on ne revient pas en arrière
"""       
    

def glouton_iterations(carrefour,plan,matrice,tmin,nb,C):
    liste = liste_phases(matrice)
    P = len(liste)
    n = len(carrefour)
    T,ve,vs = simulation(carrefour,plan,C)
    S = score(T,ve,vs)
    S1 = S
    for i in range(nb):
        N = len(plan[0])
        a = random.randint(1,4) 
        k = random.randint(0,(N-1))
        if a == 1:
            j = random.randint(0,(P-1))
            nouveau_plan = change_phase(plan,k,liste,j)
        elif a == 2:
            j = random.randint(0,(N-1))
            nouveau_plan = change_places(plan,k,j)
        elif a == 3:
            j = random.randint(0,(N-1))
            nouveau_plan = change_duree(plan,5,k,j,tmin)
        else:
            nouveau_plan = supprime_phase(plan,k)
        if nouveau_plan != plan:
            T,ve,vs = simulation(carrefour,nouveau_plan,C)
            S2 = score(T,ve,vs)
            if S2 < S:
                plan = nouveau_plan
                S1 = S2
    return(plan,S,S1)
    

def glouton_temps(S,carrefour,plan,matrice,tmin,cond,C):
    debut = time.time()
    liste = liste_phases(matrice)
    P = len(liste)
    S1 = S
    while time.time() - debut < cond:
        a = random.randint(1,4) 
        N = len(plan[0])
        k = random.randint(0,(N-1))
        if a == 1:
            j = random.randint(0,(P-1))
            nouveau_plan = change_phase(plan,k,liste,j)
        elif a == 2:
            j = random.randint(0,(N-1))
            nouveau_plan = change_places(plan,k,j)
        elif a == 3:
            j = random.randint(0,(N-1))
            nouveau_plan = change_duree(plan,5,k,j,tmin)
        else:
            nouveau_plan = supprime_phase(plan,k)
            if nouveau_plan != plan:
                N -= 1
        if nouveau_plan != plan:
            T,ve,vs = simulation(carrefour,nouveau_plan,C)
            S2 = score(T,ve,vs)
            if S2 < S:
                plan = nouveau_plan
                S1 = S2
    return(plan,S1)
  
  
  
    
""" Effectue plusieurs "petits" appels de l'algorithme naif, et garde le meilleur """
    
def glouton(carrefour,plan,matrice,tmin,nb,cond,C):
    T,ve,vs = simulation(carrefour,plan,C)
    S = score(T,ve,vs)
    S1 = S
    meilleur_plan = plan
    for i in range(nb):
        nouveau_plan,S2 = glouton_temps(S1,carrefour,plan,matrice,tmin,cond,C)
        if S2 < S1:
            meilleur_plan = nouveau_plan
            S1 = S2
    return(meilleur_plan,S,S1)
    


    
    