# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:55:33 2021
@author: natha
"""

"""Définir l'ensemble des données"""  

T = 200 #définir l'horizon global
C=0 #variable du cout global
Kr = 5 #cout de setup de la remanufacture
Km = 9#cout de setup de la manufacture
Hm = 3#cout de stockage produit manufacturé
HR = 5#cout de stockage produit prêt a être remanufacturé
        
class variable:
    #définir tous les éléments qu'on retrouve a chaque fois
        
    def __init__(self): #on définit les éléments
        self.D=50
        self.R=10
        self.t=[]
        self.xR=[]
        self.xM=[]
        self.yR=[]
        self.yM=[]
        self.GammaM=[]
        self.GammaT=[]
        
    def prod(self, xm,xr):
        self.xM=xm
        self.xR=xr


""" Création du tableau de time"""
classeur = []   
for i in range(T+1):
    classeur.append(variable())

"""Faire des test de compréhension"""

for i in range (T+1) :
    print(i)
    classeur[i].t=i
    
classeur[5].yM=3
print(classeur[18].yM)

"""Fonctions utiles"""
def net_requi(t):
    somme = 0
    for i in range (t):
        somme += (classeur[i].D-classeur[i].R)
    return somme
    somme -= classeur[0].yR  

def equa_12(t): 
    NRt=[]
    for i in range (T+1-tau):
        NRt.append(net_requi(i+tau))
    max_NRt= max(NRt)
    classeur[t].prod(max(classeur[t].D,max_NRt),0)
 
def somme_dem():
    somme=0
    for i in range (T+1):
        somme += classeur[i].D
    return somme

"""   
def equa_13(t):
    classeur[t].xM=0"""
    
# x=somme_dem()
# print(x)
    
"""Initialisation des données"""
#Demand()
tau=1 #première simulation
"""Etape 1
equa_12(tau)
equa_13(tau)
equa_2 #check ses entrées
equa_3 #check ses entrées
C=c3(tau,z) #cout initial"""

"""Etape 2"""
