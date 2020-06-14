# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:56:01 2018

@author: Josh
"""

import matplotlib.pyplot as plt
import pandas as pd


def ward_count(df, col, value, unique_id, ward_num):
    '''Returns count of unique_id in df ward_num rows w/entry value in col'''
    return df[df[col] == value].groupby("Ward")[unique_id].count()[ward_num]

def make_ward_dictionary(df, col, value, unique_id):
    '''grabs values from ward_count and makes into dictionary'''
    empty_dict = {}
    for ward in range(1, 51):
        empty_dict[ward] = ward_count(df, col, value, unique_id, ward)
    return(empty_dict)
    
    
    
with open("Crimes_-_2010_to_present.csv") as crime:
    '''First Heatmap for Crimes in Chicago by Ward'''
    df = pd.read_csv(crime, low_memory = False)
    
    intensity = make_ward_dictionary(df, "Primary Type", "NARCOTICS", "Case Number")
    row = 10
    column = 5
    count = 1
    w_array = [[0] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            w_array[i][j] = intensity[count]
            count += 1
    intens_list1 = list(intensity.values())
    max_intens1 = max(intens_list1)
            
plt.pcolor(w_array)
plt.colorbar()
plt.summer()
plt.title("Chicago Narcotics by Ward")
plt.xlabel("Ward Number Mod 5 on right")
plt.show()

    


with open("311_Service_Requests_-_Vacant_and_Abandoned_Buildings_Reported.csv") as vacant:
    '''Second Heatmap for Vacant and Abandoned Buildings in Chicago By Ward'''
    data = pd.read_csv(vacant, low_memory = False)
    
    intensity = make_ward_dictionary(data, "SERVICE REQUEST TYPE", "Vacant/Abandoned Building", "SERVICE REQUEST NUMBER")
    row = 10
    column = 5
    count = 1
    m_array = [[0] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            m_array[i][j] = intensity[count]
            count += 1
    intens_list2 = list(intensity.values())
    max_intens2 = max(intens_list2)
            
plt.figure()            
plt.pcolor(m_array)
plt.colorbar()
plt.summer()
plt.title("Chicago Vacant/Abandoned Buildings by Ward")
plt.xlabel("Ward Number Mod 5 on right")
plt.show()

                                                                                                     
'''Third Heatmap for Predictive Policing'''
third_list = []
for i in range(0, 50):
    total = intens_list1[i] / max_intens1 + intens_list2[i] / max_intens2
    third_list.append(total)
    
    
    
count2 = 0
row = 10 
column = 5
count = 1
for i in range(row):
    for j in range(column):
        m_array[i][j] = third_list[count2]
        count2 += 1
    
plt.figure()            
plt.pcolor(m_array)
plt.colorbar()
plt.summer()
plt.title("Chicago Predictive Policing")
plt.xlabel("Ward Number Mod 5 on right")
plt.show()