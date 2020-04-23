# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:15:46 2020

@author: fenixnano
"""



import pandas as pd
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# step 1:  export the colormap from Igor using the command:

'''
ColorTab2Wave IgorColormapxxx (the name of the colormap)

'''
# 
# the colormap then saved as delimited txt file 'IgorColormap01.txt'

filename = 'IgorColormap01.txt'
# name of the colormap file


# read the colormap by pandas
IgorColormap01 = pd.read_csv(filename,  sep="\t",)
# /t = tab


#IgorColormap01_8bit =  IgorColormap01/256
#IgorColormap01_8bit = IgorColormap01_8bit.astype('int32')

# convert to float in 0 :1 range
IgorColormap01_float = IgorColormap01/65536

#add alpha value
IgorColormap01_float['a'] = 1


colorlist = IgorColormap01_float.values.tolist()


cmap_name = 'IgorColormap01'

IgorColormap01 = LinearSegmentedColormap.from_list(
                    cmap_name, colorlist, N=120)

# reversed 
IgorColormap01_r = IgorColormap01.reversed()






