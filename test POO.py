# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:23:22 2021

@author: natha
"""
import copy

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
        
        
classeur = []   
for i in range(10):
    classeur.append(variable())
    classeur[i].t=i#init la temporalité
    
final = [] 
"""  
for i in range(10):
    final.append(variable())
    final[i].t=i#init la temporalité"""
    
final=copy.deepcopy(classeur)

classeur[5].D=45


        
