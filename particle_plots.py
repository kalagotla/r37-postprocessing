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

def spp(n):
    # Uses functions defined below to plot and save different figures
#    import simplecount as sc
    
    filename = 'particle.' + str(n)
    df = single_particle_data(filename)
    
#    print(df.head())
    
    # plot vel mag
    x, y = 'y', ['umag', 'vmag']
    kind='line'
    grid, legend = True, True
    xlabel, ylabel = 'Y (m)', 'Absolute Velocity (m/s)'
    axlegend = ['Fluid', 'Particle'] # To change legend
    title = []
    ax_vmag = plot_fig(df, x, y, kind, grid, legend, xlabel, ylabel, axlegend, title)
    
    # Save figure
    save_fig('vel_mag.eps', ax_vmag, n)
    
    #plot rel vel mag
    x, y = 'y', ['wmag_f', 'wmag_p']
    kind='line'
    grid, legend = True, True
    xlabel, ylabel = 'Y (m)', 'Relative Velocity (m/s)'
    axlegend = ['Fluid', 'Particle'] # To change legend
    title = []
    ax_vmag = plot_fig(df, x, y, kind, grid, legend, xlabel, ylabel, axlegend, title)
    
    # Save figure
    save_fig('rel_vel_mag.eps', ax_vmag, n)
        
    return



def single_particle_data(filename):
    # Analysis for different plots using pandas
    import pandas as pd
    import numpy as np
    """Used to plot single particle plots based on the data provided by the user"""
        
    # Count number of lines
#    n = sc.simplecount(filename)
        
    # Read in file using pandas
    # x v u a av au dt kc is the format. dt, kc (1xn) & rest (3xn)
    file_vars = ['x', 'y', 'z', 'v1', 'v2', 'v3', 'u1', 'u2', 'u3',
                 'a1', 'a2', 'a3', 'av1', 'av2', 'av3', 'au1', 'au2', 'au3',
                 'dt', 'kc']
    df = pd.read_csv(filename, names = file_vars, delim_whitespace=True)
#    print(df.head())
        
    # Create and append new data into dataframe
    df['xf'] = df['x']*df['dt'].cumsum() # Fluid x position
    df['yf'] = df['y']*df['dt'].cumsum() # Fluid y position
    df['zf'] = df['z']*df['dt'].cumsum() # Fluid z position
    # Velocity magnitudes
    df['vmag'] = np.sqrt(df['v1']**2 + df['v2']**2 + df['v3']**2) # Particle
    df['umag'] = np.sqrt(df['u1']**2 + df['u2']**2 + df['u3']**2) # Fluid
    # Relative quantities
    """Hardcoding U velocity. Need to replace this with file/usr input"""
    u_rotor = 317.898 #m/s
    # Velocity magnitudes
    df['wmag_p'] = np.sqrt(df['v1']**2 + df['v2']**2 + (df['v3']-u_rotor)**2)
    df['wmag_f'] = np.sqrt(df['u1']**2 + df['u2']**2 + (df['u3']-u_rotor)**2)
    # Mach numbers
#    df['relmach_p'] = df['wmag_p']/np.sqrt(1.4*287.058*df)
    
        
    
    return df


def plot_fig(df, x, y, kind, grid, legend, xlabel, ylabel, axlegend, title):
    # plot data
    # title is another option that can be used
    ax = df.plot(x=x, y=y, kind=kind, grid=grid, legend=legend, title=title)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.legend(axlegend) # To change legend
    
    return ax


def save_fig(result_name, ax, n):
    import os
    
    # Save figure
#    script_dir  = os.path.dirname(__file__) # Current file location
    script_dir  = os.getcwd()
    results_dir = os.path.join(script_dir, 'particle' + str(n) + '_results/')
    
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
    
    ax.figure.savefig(results_dir + result_name, format='eps')
    
    return

