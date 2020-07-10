import tensorflow as tf
import numpy as np
import matplotlib.patches as mp
import matplotlib.pyplot as pl
pl.rcParams['figure.figsize'] = (10,6)

X = np.arange(0.0, 5.0, 0.2)
a=3
b=2
Y=a*X+b
pl.plot(X,Y)
pl.ylabel('y')
pl.xlabel('x')
pl.show()