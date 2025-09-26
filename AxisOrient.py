
from vpython import *
import numpy as np

arrowL = 2
arrowT = 0.02
theta = 0
pntT = 0.4

Xarrow = arrow(axis = vector(1, 0, 0), color = color.red, lenght = arrowL, shaftwidth = arrowT)
Yarrow = arrow(axis = vector(0, 1, 0), color = color.red, lenght = arrowL, shaftwidth = arrowT)
Zarrow = arrow(axis = vector(0, 0, 1), color = color.red, lenght = arrowL, shaftwidth = pntT)

pntArrow = arrow (axis = vector (arrowL * np.cos (theta), arrowL * np.sin (theta)), color = color.orange, length = arrowL, shaftwodth = arrowT)

while True:
  for myAngle in np.linspace(0, 2 * np.pi, 100):
    rate(50)
    pntArrow.axis = vector(arrowL * np.cos(myAngle), arrow * np.sin(myAngle), 0)
    pntArrow.lenght = arrowL
    
    
