# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:55:33 2021
@author: natha
"""
import pandas as pd
"""Définir l'ensemble des données"""  

T = 200 #définir l'horizon global
C=0 #variable du cout global
Kr = 5 #cout de setup de la remanufacture
Km = 9#cout de setup de la manufacture
Hm = 3#cout de stockage produit manufacturé
Hr = 5#cout de stockage produit prêt a être remanufacturé
        
class variable: #définir tous les éléments qu'on retrouve a chaque fois        
    def __init__(self): #on définit les éléments
        self.D=50
        self.R=30
        self.t=0
        self.xR=0
        self.xM=0
        self.yR=0
        self.yM=0
        self.GammaM=0
        self.GammaR=0
        self.NR=0
        
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
    return somme
        
# def init_loi():
#     u=1
    
#def export():
#     u=1
    
# def import_data():
#     u=1

def init_t0(t):
    classeur[t-1].yR=0#t-1 car on se place avant tau
    classeur[t-1].yM=0
    

def search_l(k):
    for i in range (k-tau):
        if classeur[i+tau].xM>0:
            point=classeur[i+tau].t
    return point
"""générer aléatoire les données"""
    


"""Equations"""

def equa_2(t):
    classeur[t].yR=classeur[t-1].yR+classeur[t].R-classeur[t].xR
    
def equa_3(t):
    classeur[t].yM=classeur[t-1].yM+classeur[t].xR+classeur[t].xM-classeur[t].D
    
def equa_11(t):
    somme = 0
    for i in range (t):
        somme += (classeur[i].D-classeur[i].R)
    return somme
    somme -= classeur[0].yR
    classeur[t].NR=somme

def equa_12(t): 
    NRt=[]
    for i in range (T+1-tau):
        NRt.append(equa_11(i+tau))
    max_NRt= max(NRt)
    classeur[t].prod(max(classeur[t].D,max_NRt),0)
    
def equa_13(t):
    sommeX =0
    for i in range (t-1-tau):
        sommeX+=classeur[i+tau].xR
    classeur[t].xR=max(somme_dem(tau, t)-sommeX-classeur[tau].xM,0)
    classeur[t].xM=1
    
def equa_14():
    for i in range (len(classeur)):#Obtenir la variable binaire correspond a l'utilisation ou non
        if classeur[i].xM>0:
            classeur[i].GammaM=1
        else :
            classeur[i].GammaM=0
        if classeur[i].xR>0:
            classeur[i].GammaR=1
        else :
            classeur[i].GammaR=0
    somme=0
    somme+= Km
    for i in range (z-tau):
        somme += classeur[i].GammaR*Kr
        somme += classeur[i].yM*Hm
        somme += classeur[i].yR*Hr
    somme=somme/(z-tau+1)
    return somme
    
# x=somme_dem()
# print(x)
    
"""Initialisation des données"""
#Demand()
tau=1 #temporalité de la première simulation
z= T
init_t0(tau)

"""Etape 1 : find initial schedule"""
for i in range (len(classeur)):#NRt pour tout le planning
    equa_11(i)
equa_12(i) #XR_tau a 0, et XM_tau selon max(D/NR)
for i in range (len(classeur)): #Xmt=0, xrt>=0, selon demande....
    equa_13(i)
for i in range(len(classeur)-1):
    equa_2(i+1)
for i in range(len(classeur)-1):
    equa_3(i+1)
Cini=equa_14()

final=classeur
"""Etape 2"""
DeltaCI=[]
DeltaCII=[]
for k in range (z-(tau-1)): 
    if classeur[k].xR>0 :
        classeur[tau].xM+= classeur[tau].xR
        classeur[k].xR=0
        for i in range (k-(tau-1)):
            equa_13(i)
            for t in range(len(classeur)):
                equa_2(t)
                equa_3(t)
        DeltaCI.append(equa_14()-Cini)
        #reset initial schedule
        l=search_l(k)
           
        if classeur[l].yR>=classeur[k].xR:
            classeur[l].xR+=classeur[k].xR
            classeur[k].xR=0
        else :
            classeur[tau].xM+=classeur[k].xR-classeur[l].yR
            classeur[l].xR+=classeur[l].yR
            classeur[k].xR=0
        for t in range(len(classeur)):
                equa_2(t)
                equa_3(t)
        DeltaCII.append(equa_14()-Cini)     

"""Etape 3"""
"""if min
implement the best schedule
Cini=Cini + min
go to step 2
end if"""
