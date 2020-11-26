# program to plot graphs
import math
import matplotlib.pyplot as plt
# define the funtion 
def f(x):
    return x**2
# number of data points
n=100
a=[0]
b=[f(a[0])]
# step size
h=0.1

for i in range(1,n):
    x0=a[i-1]+h
    a.append(x0)
    y0=f(x0)
    b.append(y0)

plt.plot(a,b)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.title('function in graph')# change graph name 
plt.show()


