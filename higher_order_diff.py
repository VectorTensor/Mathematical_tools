# Higher order differential equation using euler method or RK-2. This is the program that goes up to second order but 
# it can be scaled up to make it work for higher order 
import math 
import matplotlib.pyplot as plt 

#Function F1 used for m z= dy/dx
def F1(z):
    return z
#Function F2 dz/dx=F2
def F2(x,y,z):
    return 6*x+ 3*y - 2*z

#Initiating data
x0=0 # Initial values for x,y,z where z=dy/dx
y0=0
z0=1
a=[x0]
b=[y0]
c=[z0]
h=0.2 # Step size 
#Rk-2 or euler function 

def y(x0,y0,z0):
    m1=F1(z0)
    l1=F2(x0,y0,z0)
    m2=F1(z0+l1*h)
    l2=F2(x0+h,y0+h*m1,z0+l1*h)
    m=(m1+m2)/2
    l=(l1+l2)/2
    y=y0+m*h
    z=z0+l*h
    return [y,z]

for i in range(0,20):
    it = y(x0,y0,z0)
    x0=x0+h
    a.append(x0)
    y0= it[0]
    z0= it[1]
    b.append(y0)
    c.append(z0)
print(b) 
plt.plot(a,b)# Plotting using matplotlib 
plt.xlabel('x') # Edit x and y label and title of the graph 
plt.ylabel('f(x)')
plt.title('Solution to the differential equation')
plt.grid('both')# Enable or disable graph
plt.show()
   


