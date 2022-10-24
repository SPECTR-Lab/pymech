#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:19:22 2022

@author: anton
"""

from pymech.neksuite import readrea
import numpy as np
import matplotlib.pyplot as plt

# Read in file, create object and print
fn = "box.rea"
d = readrea(fn)
print(d)

# Extract data from object
nel = d.nel
ndim = d.ndim
lims = d.lims.pos
pos = np.array([i.pos for i in d.elem]) # x,y,z
#print(pos[0])

# Extract boundary conditions
bc = []
sides = 4
for j in range(nel): # Iterate through each element
    bb = d.elem[j].bcs
    for side in range(sides): # Iterate through each side
        a = bb[0][side][0]
        b = repr(a)
        c = str(b)
        c = c.lstrip("'"); c = c.rstrip("'");                       
        bc.append(c)    

# Find boundaries
pointsX = []; pointsY = [];
X = []; Y = [];
for k in range(nel): # iterate through each element

    pointsX.append(pos[k, 0, 0, 0, 0]) 
    pointsX.append(pos[k, 0, 0, 0, 1])
    pointsX.append(pos[k, 0, 0, 1, 1]) 
    pointsX.append(pos[k, 0, 0, 1, 0])
    
    pointsY.append(pos[k, 1, 0, 0, 0]) 
    pointsY.append(pos[k, 1, 0, 0, 1])
    pointsY.append(pos[k, 1, 0, 1, 1]) 
    pointsY.append(pos[k, 1, 0, 1, 0])

    xc1 = (pos[k, 0, 0, 0, 0] + pos[k, 0, 0, 0, 1]) / 2.0
    xc2 = (pos[k, 0, 0, 0, 1] + pos[k, 0, 0, 1, 1]) / 2.0
    xc3 = (pos[k, 0, 0, 1, 1] + pos[k, 0, 0, 1, 0]) / 2.0
    xc4 = (pos[k, 0, 0, 1, 0] + pos[k, 0, 0, 0, 0]) / 2.0
    
    yc1 = (pos[k, 1, 0, 0, 0] + pos[k, 1, 0, 0, 1]) / 2.0
    yc2 = (pos[k, 1, 0, 0, 1] + pos[k, 1, 0, 1, 1]) / 2.0
    yc3 = (pos[k, 1, 0, 1, 1] + pos[k, 1, 0, 1, 0]) / 2.0
    yc4 = (pos[k, 1, 0, 1, 0] + pos[k, 1, 0, 0, 0]) / 2.0
    
    X.append(xc1); X.append(xc2); X.append(xc3); X.append(xc4);
    Y.append(yc1); Y.append(yc2); Y.append(yc3); Y.append(yc4);   

# Plot

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 3,
        }

pointsnpX = np.asarray(pointsX)
pointsnpY = np.asarray(pointsY)

fig, ax = plt.subplots(figsize=(20,15), dpi=800)
plt.xticks(np.arange(-8, 24.1, step=4))
plt.grid(color='gray', linestyle='--', linewidth=0.2)
plt.title('New BC\'s Outer Mesh')
for xp, yp, m in zip(X, Y, bc):
    plt.text(xp,yp,m, fontdict=(font))
plt.plot(pointsnpX, pointsnpY, linestyle='None', marker = '.', color = 'k', markersize=2) 
plt.show()

image_format = 'svg' # e.g .png, .svg, etc.
image_name = 'mesh.svg'

fig.savefig(image_name, format=image_format, dpi=1200)