# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:21:59 2021

@author: natha
"""

import pandas as pd

""" EXemp exp"""

data = {'Product': ['Desktop Computer','Tablet','Printer','Laptop'],
        'Price': [850,200,150,1300]
        }

df = pd.DataFrame(data, columns= ['Product', 'Price'])

df.to_csv (r'D:\Nathan\Documents\Git\GP27-project\export_dataframe.csv', index = False, header=True)

#print (df)

df2 = pd.read_csv (r'D:\Nathan\Documents\Git\GP27-project\export_dataframe.csv')
print (df2)