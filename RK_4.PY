# Solution of first order differential equation using RK-4 method S
import math
import matplotlib.pyplot as plt
#function dy/dx=f(x,y)
def f(x,y):
    return (1+x**2)*y
h=0.02 #Step size  
x0=0 #initial value f(x0)=y0
y0=1
a=[x0]
b=[y0]
def y(x0,y0): #RK-4 Iteration function
    m1=f(x0,y0)
    m2=f(x0+(h/2),y0+(h/2)*m1)
    m3=f(x0+(h/2),y0+m2*(h/2))
    m4=f(x0+h,y0+m3*h)
    m=(m1+2*m2+2*m3+m4)/6
    
    y1=y0+h*m
    return y1  

for i in range(1,100):
    it=y(x0,y0)
    x0=x0+h
    a.append(x0)
    y0=it
    b.append(y0)

print (b)

plt.plot(a,b,color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid('both')
plt.title('Solution to the differential equation')
plt.show()
