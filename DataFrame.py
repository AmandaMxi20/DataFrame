# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 03:58:21 2020

@author: Zibonele
"""


import pandas as pd
#initialise data of lists
data = {'Packages':['Chips','Cooldrinks','Chocolates','Pies','Fruit','Cupcakes',
        'Veggies'], 'Product1':['Simba','Coke','Cadbury','Pepper','Pear',
                                'Vanilla','Spinach'],
                                'Product2':['Lays','Fanta','Tex','Steak','Apple',
          'Vanilla','Spinach'  ],
            'Product3':[' ',' ',' ','Chicken ','Orange', ' ',' ']}
                                
 #Create a dataFrame
df = pd.DataFrame(data,index =['a','b','c','d','e','f','g'])

#Print the output
print(df)


                                            