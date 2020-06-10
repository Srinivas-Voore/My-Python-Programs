import numpy as np
x=np.ones((5,5))
y=np.zeros((3,3))
y[1,1]=9
x[1:-1,1:-1]=y
print(x)
