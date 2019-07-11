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
    import particle_plots as pp
    
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
    
    
    print('\n&&&&&&&  Welcome to Rotor 37 post-processing scrpit  &&&&&&&\n',
          '\nPlease choose a number from below to perform an action:',
          '\n 1. Contours',
          '\n 2. Single particle plots',
          '\n 3. Tecplot data files (plot3d data)',
          '\n 4. Location plots')
    
    usr_selection = input()
    print('usr_selection=', usr_selection)
    
    if int(usr_selection) == 2:
        # A loop to go through all particle files. Later can be modified for parallel processing -- Check OneNote
#        print('Using usr value as 2 to spawn ' + str(N) + ' particles')
        for i in range(N):
#            print('for loop is good and using ' + str(i+1))
            pp.spp(i+1)
    
    return N