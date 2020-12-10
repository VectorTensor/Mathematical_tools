import numpy as np
import matplotlib.pyplot as plt
#function 
def f(x,y):
    return x**2 - y**2

#Data 
x= np.arange(-100,100,0.1)
y=np.arange(-100,100,0.1)
#Making meshgrid
X,Y=np.meshgrid(x,y)
u= f(X,Y)
plt.contour(x,y,u)
plt.title('Contour plot')#Names
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.show()

