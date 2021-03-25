# coding: utf-8
import random
import time

""" Algorithme heuristique : Descente à voisinage variable -> Première version"""


#Fonction auxiliaire effectuant le parcours dans un voisinage, chaque voisinage correspondant à une des quatre fonctions pour modifier le plan de feux

def voisinage1(m,N,P,S,matrice,carrefour,plan,liste,tmin,C):
    k = random.randint(0,(N-1))
    modif = False                                        #Un booléen servant uniquement à savoir si l'on diminue le nombre de phases ou non
    if m == 0:                                           #Disjonction de cas selon le voisinage dans lequel on se trouve
        j = random.randint(0,(P-1))
        nouveau_plan = change_phase(plan,k,liste,j)
    elif m == 1:
        j = random.randint(0,(N-1))
        while j == k:
            j = random.randint(0,(N-1))
        nouveau_plan = change_places(plan,k,j)
    elif m == 2:
        j = random.randint(0,(N-1))
        while j == k:
            j = random.randint(0,(N-1))
        nouveau_plan = change_duree(plan,5,k,j,tmin)
    else:
        nouveau_plan = supprime_phase(plan,k)
        if nouveau_plan != plan:
            modif = True
    if nouveau_plan != plan:                                    #On regarde si la fonction auxiliaire appelée a renvoyé un plan différent
        T,ve,vs = simulation(carrefour,nouveau_plan,C)          
        S1 = score(T,ve,vs)
        if S1 < S:                      #On regarde si ce plan est meilleur que le précédent, si c'est le cas on repart au premier voisinage (m = 0)
            if modif:                                            
                return(nouveau_plan,S1,0,N-1)
            else:
                return(nouveau_plan,S1,0,N)
    return(plan,S,(m+1)%4,N)            #Sinon on passe au voisinage suivant
            
            
    

""" L'algorithme d'optimisation en lui même qui apelle la fonction auxiliaire tant que le temps de calcul voulu n'a pas été dépassé
    On parcourt donc les voisinages, selon si on trouve une meilleure solution ou non
    Dans chaque voisinage, on effectue une modification aléatoire, on regarde si elle permet une amélioration ou non
    Si elle permet une amélioration, on repart au premier voisinage
    Sinon, on passe au voisinage suivant
"""
    
    

def VND1(carrefour,plan,matrice,tmin,cond,C):
    liste = liste_phases(matrice)
    optimise(liste)
    P = len(liste)
    n = len(carrefour)
    N = len(plan[0])
    T,ve,vs = simulation(carrefour,plan,C)
    S = score(T,ve,vs)
    S1 = S
    m = 0
    debut = time.time()
    while time.time()-debut < cond:
        plan,S1,m,N = voisinage1(m,N,P,S1,matrice,carrefour,plan,liste,tmin,C)
    return(plan,S,S1)
        
        
        
        

""" Avantages de l'algorithme :
    -Assez simple a mettre en place une fois la structure de voisinages bien définie, la situation ici s'y prête très bien
    -En une durée assez courte (10 secondes) renvoie systématiquement une meilleure solution que celle renvoyée par l'algorithme glouton
"""