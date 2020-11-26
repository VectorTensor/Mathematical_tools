import numpy as np
import matplotlib.pyplot as plt

x1=[5,7,11,13,17]
y=[150,392,1452,2366,5202]
def fun(x):
    fun=0
    
    for i in range(0,5):
        A=1
        B=1
        for j in range(0,5):
            if (i != j):
                A=A*(x-(x1[j]))

        for j in range(0,5):
            if (i != j):
                B=B*(x1[i]-x1[j])
        fun=fun + (A/B)*y[i]                
    return fun    

a=[5]
b=[fun(5)]
print(b[0])
for i in range(1,500):
    a.append(a[i-1]+0.01)
    b.append(fun(a[i]))

plt.plot(a,b)
plt.show()





