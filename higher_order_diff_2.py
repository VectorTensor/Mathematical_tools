#Solution of higher order differential equation using RK-4 method. This program can is for second order ode. This can be scaled in order to use it for higher
#order
import math
import matplotlib.pyplot as plt

#Function F1 used for m z= dy/dx
def F1(z):
    return z
#Function F2 dz/dx=F2
def F2(x,y,z):
    return math.sin(x)+3*z-y

#Initiating data
x0=1 # Initial values for x,y,z where z=dy/dx
y0=1.2
z0=0.5
a=[x0]
b=[y0]
c=[z0]
h=0.2 # Step size 

#RK-4 Function 

def y(x0,y0,z0):
    m1=F1(z0)
    l1= F2(x0,y0,z0)
    m2=F1(z0+(h/2)*l1)
    l2=F2(x0+(h/2),y0+(h/2)*m1,z0+(h/2)*l1)
    m3=F1(z0+(h/2)*l2)
    l3=F2(x0+h/2,y0+(h/2)*m2,z0+(h/2)*l2)
    m4=F1(z0+(h)*l3)
    l4=F2(x0+h,y0+m3*h,z0+l3*h)
    m=(m1+2*m2+2*m3+m4)/6
    l=(l1+2*l2+2*l3+l4)/6
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
      

















