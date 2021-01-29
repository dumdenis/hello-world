#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:51:12 2020

@author: dumontdenis
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

directory="/Users/dumontdenis/Dropbox/Recherche/1-GranularMatter/4-Heap and Inclined flow/Analyse/Inclined Plane/VelocityProfile and theta R dependance/R"
list_theta_c=[21,19.5,18.5,19,18.5,19,19,21,20.5,21.5]
#list_theta_c=[23,19,19,19,19,19,20,21,20.5,21.5]
listR=[3,5,7,8,9,10,11,12,15,20]

datalow=pd.DataFrame()
datahigh=pd.DataFrame()

for i,R in enumerate(listR):
    theta_c=list_theta_c[i]
    #Extraction of the data
    path=directory+str(R)+"_short/MeanLayerProperties.txt"
    tab=pd.DataFrame()
    data=pd.read_csv(path,sep=',',header=0,index_col=None,skiprows=0)
    line=pd.concat([data.iloc[:,0:5]],axis=1)
    tab=pd.concat([tab,line],axis=0)

    path=directory+str(R)+"_short/mu_I.txt"
    tab2=pd.DataFrame()
    data=pd.read_csv(path,sep=',',header=0,index_col=None,skiprows=0)
    line=pd.concat([data.iloc[:,0:3]],axis=1)
    tab2=pd.concat([tab2,line],axis=0)

    tab_full_data=pd.concat([tab,tab2],axis=1)
    tab_full_data.to_csv("R"+str(R)+"_full_data.csv",index=False)
#    print(tab_full_data.head())
