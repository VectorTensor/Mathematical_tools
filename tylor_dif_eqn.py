def y1(x):
    return (x**3+2)

def y2(x,yo):

    return (3*x**2)*yo



y=3
y1=y1(3)
y2=y2(3,y1)

ans = y+0.2*y1+((0.2**2)/2)*y2
print (ans)