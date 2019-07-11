#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:36:01 2019

@author: kal @ Dilip Kalagolta (kalagodk@mail.uc.edu)

Add code summary below:
    Single particle plots are generated using particle.N files
    Various plots will be generated
    User will have the option to choose to save individual files or all at once
"""

def spp(N):
#    import simplecount as sc
    import numpy as np
    import pandas as pd
    from dask import dataframe as dd
    import matplotlib.pyplot as plt
    
    # Internal function. Call in this file only
    def single_particle_plots(filename):
        """Used to plot single particle plots based on the data provided by the user"""
        
        # Count number of lines
#        n = sc.simplecount(filename)
        
        # Read in file using pandas
        # x v u a av au dt kc is the format. dt, kc (1xn) & rest (3xn)
        file_vars = ['x', 'y', 'z', 'v1', 'v2', 'v3', 'u1', 'u2', 'u3',
                    'a1', 'a2', 'a3', 'av1', 'av2', 'av3', 'au1', 'au2', 'au3',
                    'dt', 'kc']
        df = pd.read_csv(filename, names = file_vars, delim_whitespace=True)
        print(df.head())
        
        # plot data
        ax = df.plot(x='x', y=['v1', 'u1'], kind='line', title='Path', grid=True,
                     legend=False)
        ax.set(xlabel='X (m)', ylabel='Y (m)')
#        ax.set_xlabel('X')
#        ax.set_ylabel('Y')
#        ax.legend(['X', 'Y']) # To change legend
        return


    # Number of lines in particle.N file
    filename = 'particle.' + str(N)
    print("I'm working!")
    single_particle_plots(filename)
        
        
        
        
    
    return