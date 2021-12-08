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
        
class variable: #définir tous les éléments qu'on retrouve a chaque fois
        
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
    classeur[i].t=i#init la temporalité

"""Faire des test de compréhension"""
# for i in range (T+1) :
#     print(i)
#     classeur[i].t=i
    
# classeur[5].yM=3
# print(classeur[18].yM)

"""Fonctions utiles"""
def somme_dem(i,n):
    somme=0
    for k in range (n-i):
        somme+= classeur[k+i].D
    


"""Equations"""
def equa_11(t):
    somme = 0
    for i in range (t):
        somme += (classeur[i].D-classeur[i].R)
    return somme
    somme -= classeur[0].yR  

def equa_12(t): 
    NRt=[]
    for i in range (T+1-tau):
        NRt.append(equa_11(i+tau))
    max_NRt= max(NRt)
    classeur[t].prod(max(classeur[t].D,max_NRt),0)
    
def equa_13(t):
    sommeX =0
    for i in range (t-1-tau):
        sommeX-=classeur[i+tau]-classeur[tau].xM
    classeur[t].xR=max(somme_dem(tau, t)-sommeX,0)
    classeur[t].xM=0
 

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
tau=1 #temporalité de la première simulation
z= T
"""Etape 1"""
# equa_12(tau)
# equa_13(tau)
# equa_2 #check ses entrées
# equa_3 #check ses entrées
# C=c3(tau,z) #cout initial

"""Etape 2"""
"""
for k in range (z-(tau-1)):
    if classeur[k].xR>0 :
        classeur[tau].xM+= classeur[tau].xR
        classeur[k].xR=0
        for i in range (k-(tau-1)):
            l=k-2 #faire une fonction search_l
            #update xr(i) using equa_13
            #update ym(t) et yr(t) avec equa_2 et equa_3
        #determine delta C1 avec C3()
        #reset initial schedule
        #Find period l (period of the last remanufacturing lot before period k)
        if classeur[l].yR>=classeur[k].xR:
            classeur[l].xR+=classeur[k].xR
            classeur[k].xR=0
        else :
            classeur[tau].xM+=classeur[k].xR-classeur[l].yR
            classeur[l].xR+=classeur[l].yR
            classeur[k].xR=0
        #update ym(t) et yr(t) avec 2 et 3
        #determine delta C2"""
#fin    

"""Etape 3"""
"""if min
implement the best schedule
Cini=Cini + min
go to step 2
end if"""
