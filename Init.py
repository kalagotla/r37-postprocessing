#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:09:15 2019

@author: kal @ Dilip Kalagotla (kalagodk@mail.uc.edu)

Add code summary below:
    This script walks user through the code and has some variables to pass
"""

def init():
    # This script is for user interaction with the post-processing script
    
    import subprocess
    import os
    import re
    
    # Find max. no. of particles by max file number "N"
    max_N = lambda: subprocess.Popen("ls particle.* | sort -rn | head -1 | awk -F'[.]' '{print $2}'",
                                     shell=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)
    
    # Loop to assign working directory and find out number of particles spawned
    print('Is this the working directory? (y/n)')
    while True:
        l_wrdir = input() # logic variable
        if l_wrdir == 'y':
            # Getting integer out of max_N output
            N = max_N().communicate()[0].decode('ascii')
            N = int(re.search(r'\d+', N).group())
            break
        elif l_wrdir == 'n':
            print('Please specify the working directory.',
                  '\nInput relative path from current directory')
            wrdir = input()
            try:
                # Change the current working Directory
                os.chdir(wrdir)
                print("Directory changed")
                N = max_N().communicate()[0].decode('ascii')
                N = int(re.search(r'\d+', N).group())
            except OSError:
                print("Can't change the Current Working Directory")
            break
        print('This really is a dumb system. Please enter y/n.\n')
    
    # Usr interface heirarchy
    print('\n&&&&&&&  Welcome to Rotor 37 particle post-processing scrpit  &&&&&&&\n',
          '\nPlease choose a number from below to perform an action:',
          '\n 1. Contours',
          '\n 2. Single particle plots',
          '\n 3. Tecplot data files (plot3d data)',
          '\n 4. Location plots')
    
    usr_selection = input()
    if int(usr_selection) == 2:
        # Plot n number of particles
        print('Number of particles to plot? If all input 0,',
              'If you want to select particle individually input a negative number')
        particle_no = 0 # Variable for individual particles
        no_of_particles = int(input())
        if no_of_particles == 0 or no_of_particles >= N:
            no_of_particles = N
            plot_particles(no_of_particles, particle_no)
        elif 0 < no_of_particles <= N:
            plot_particles(no_of_particles, particle_no)
            
        # Plot given particle number
        while no_of_particles < 0:
            print('Enter particle number. If done enter 0.')
            particle_no = int(input())
            if particle_no == 0:
                print('Done with single particle plots.')
                no_of_particles = 7 # Some positive number
                particle_no = -7 # Some negative number
            elif particle_no > 0:
                plot_particles(no_of_particles, particle_no)
            
            
    return N
    

def plot_particles(no_of_particles, particle_no):
    import particle_plots as pp
    # A loop to go through all particle files. Later can be modified for parallel processing -- Check OneNote
    if no_of_particles >= 0:
        for i in range(no_of_particles):
            pp.spp(i+1)
    elif no_of_particles < 0:
        pp.spp(particle_no)
    
    return