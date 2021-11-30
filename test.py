# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:55:33 2021
@author: natha
"""
T = 200 #définir l'horizon global

class variable:
    #définir tous les éléments qu'on retrouve a chaque fois
    def __init__(self):
        self.D=[]
        self.t=[]
        self.R=[]
        self.xR=[]
        self.xM=[]
        self.yR=[]
        self.yM=[]
        self.GammaM=[]
        self.GammaT=[]

"""        
def Demand:
Faire une fonction qui va remplir chaque demande
"""

classeur = [variable]*(T+1)

def net_requi(t):
    somme = 0
    for i in range (t):
        somme += (classeur[i].D-classeur[i].R)
    somme -= classeur[0].yR    


        


