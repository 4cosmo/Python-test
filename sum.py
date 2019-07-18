import math

for i in range(1,2000000):
    ya = i/10000
    yb = ya
    deg_a = math.asin(ya/350)
    deg_b = math.asin(ya/250)
    xa = 350*math.cos(deg_a)
    xb = 250*math.cos(deg_b)
    t = xa+xb
    if t >= 459.0 and t <=459.00001 :
        print(t,":",xa,":",xb,":",ya,math.degrees(deg_a),math.degrees(deg_b))

#math.radians(0.5)
