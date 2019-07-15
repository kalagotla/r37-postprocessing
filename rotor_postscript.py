#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:38:45 2019

@author: kal @ Dilip Kalagotla (kalagodk@mail.uc.edu)

Add code summary below:
    main program for the post-processing
    All modules will be called in here
"""

def rotor_ps():
    import time
    import Init as init
    import os
    import particle_plots as pp
    
    start_time = time.time()
    wrdir = os.getcwd()
    
    N = init.init()
    print('Number of particles counted = ', N)
#    pp.spp(N)
    
    end_time = time.time()
    
    print('Time taken: ', end_time-start_time)
    
#    print('Is this the working directory? (y/n)')
    # Changing wdir back to current dev folder
    os.chdir(wrdir)
    print("\nWdir set to default location")
    
    return

rotor_ps()