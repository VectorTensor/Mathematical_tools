import math
import matplotlib.pyplot as plt
#function dy/dx=f(x,y)
def f(x,y):
    return math.sin(x)+math.cos(y)
h=0.5 #Step size  
x0=0 #initial value f(x0)=y0
y0=2
a=[x0]
b=[y0]
def y(x0,y0): #RK-2 Iteration function
    m1=f(x0,y0)
    m2=f(x0+h,y0+h*m1)
    y1=y0+h*(m1+m2)/2
    return y1    

for i in range(1,10):
    it=y(x0,y0)
    x0=x0+h
    a.append(x0)
    y0=it
    b.append(y0)
xnum=0.5
index=0
print (b)
for i in range(0,10):
    if (xnum==a[i]):
        index=i


plt.annotate('data point',(xnum,b[index]))
plt.plot(a,b,color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid('both')
plt.title('Solution to the differential equation')
plt.show()
