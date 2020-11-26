# solution of differential equation using taylor's method
# the main function dy/dx
def y1(x):
    return (x**3+2)
# the second derivative
def y2(x,yo):

    return (3*x**2)*yo


#initial condition 
y=3
y1=y1(3)
y2=y2(3,y1)
# implementation of the formula the value of y next step
ans = y+0.2*y1+((0.2**2)/2)*y2
print (ans)