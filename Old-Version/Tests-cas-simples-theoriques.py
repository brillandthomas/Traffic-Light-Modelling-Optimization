#coding: utf-8

""" On réalise d'abord des tests théoriques simplistes pour voir si les simulations + optimisations sont convenables 

1) Une route à deux sens, pas de croisement, on met un plan tel qu'un seul des deux feux soit au vert,
    la route est telle que le flux de voitures est important
    on s'attend à ce que l'optimisation mène à une phase unique avec les deux feux au vert 
"""

matrice1 = [[1,1],[1,1]]
carrefour1 = [(1/6,1),(1/6,1)]
plan1 = ([([1,0],30),([0,1],30),([1,0],20),([0,1],20)],100)


""" Ici l'algorithme glouton suffit largement, et résout très rapidement et correctement le problème 


2) Un croisement, 4 flux, 2 flux  ----> une route plus fréquentée que l'autre
    on s'attend à ce que l'optimisation mène à 2 phases, avec une durée de phase plus grande pour la route plus fréquentée
"""

matrice2 = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
carrefour2 = [(1/4,1),(1/4,1),(1/6,1),(1/6,1)]
plan2 = ([([1,0,0,0],20),([0,1,0,0],20),([0,0,1,0],20),([0,0,0,1],20)],80)

""" L'algorithme glouton renvoie un résultat moins bon que l'algorithme VND
Mais les deux renvoient un résultat cohérent et bien meilleur que l'original"""


