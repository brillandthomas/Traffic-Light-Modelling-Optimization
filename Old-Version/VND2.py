# coding utf-8

""" Deuxième version de l'algorithme VND, cette fois il n'y a que 3 voisinages : 
    -> changement de places, changement de phase et suppresion de phase
    on utilise la fonction change_duree comme une descente locale, avec un algorithme glouton, qu'on réitère un certain nombre de fois"""


def local(S,carrefour,plan,tmin,dt,ite,C):
    S1 = S
    N = len(plan[0])
    for i in range(ite):
        k = random.randint(0,N-1)
        j = random.randint(0,N-1)
        while j == k:
            j = random.randint(0,N-1)
        nouveau_plan = change_duree(plan,dt,k,j,tmin)
        if nouveau_plan != plan:
            T,ve,vs = simulation(carrefour,nouveau_plan,C)
            S2 = score(T,ve,vs)
            if S2 < S1:
                plan = nouveau_plan
                S1 = S2
    return(nouveau_plan,S1)




def VND(carrefour,plan,matrice,tmin,dt,duree,ite,C):
    debut = time.time()
    liste = liste_phases(matrice)
    P = len(liste)
    T,ve,vs = simulation(carrefour,plan,C)
    S = score(T,ve,vs)
    S1 = S
    m = 0
    while time.time()-debut < duree:
        N = len(plan[0])
        if m == 0:
            i = 0
            k = random.randint(0,N-1)
            j = random.randint(0,P-1)
            nouveau_plan = change_phase(plan,k,liste,j)
            while i < ite and nouveau_plan == plan:
                j = random.randint(0,P-1)
                nouveau_plan = change_phase(plan,k,liste,j)
                i+=1
            nouveau_plan,S2 = local(S1,carrefour,nouveau_plan,tmin,dt,ite,C)
            if S2 < S1:
                plan = nouveau_plan
                S1 = S2
            else:
                m+=1
        elif m == 1:
            k = random.randint(0,N-1)
            j = random.randint(0,N-1)
            while j == k:
                j = random.randint(0,N-1)
            nouveau_plan = change_places(plan,k,j)
            nouveau_plan,S2 = local(S1,carrefour,nouveau_plan,tmin,dt,ite,C)
            if S2 < S1:
                plan = nouveau_plan
                S1 = S2
                m = 0
            else:
                m+=1
        else:
            i = 0
            k = random.randint(0,N-1)
            nouveau_plan = supprime_phase(plan,k)
            while i < ite and nouveau_plan == plan:
                k = random.randint(0,N-1)
                nouveau_plan = supprime_phase(plan,k)
                i+=1
            if nouveau_plan != plan:
                nouveau_plan,S2 = local(S1,carrefour,nouveau_plan,tmin,dt,ite,C)
            else:
                S2 = S1
            if S2 < S1:
                plan = nouveau_plan
                S1 = S2
            m = 0
    return(plan,S,S1)
    
    
    