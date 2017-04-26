import math
import numpy as np
import matplotlib.pyplot as plt

x = input("Enter a : ")
y = input("Enter b : ")
n = input("Enter n : ")
r = math.hypot(x, y)
theta = math.asin(y/r)

roots =[]
if n >= 2:
    for k in range((n)):
        root = math.pow(r, 1.0/n)
        a = root * math.cos((theta/n + (2*math.pi*k)/n))
        b = root * math.sin((theta/n + (2*math.pi*k)/n))
        roots.append([a,b])

print("Coefficients of Roots :",roots)

thetas = []
for i in enumerate(roots):
    print(i)
    w, k = roots[i[0]]
    thetas.append(np.arctan2(k,w))
    thetas.append(0)

z = []
theta = thetas
for i in enumerate(roots):
    z.append(r*10)
    z.append(0)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, z, linewidth=.2)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)
ax.set_title("Complex Roots on a Polar Plane", va='bottom')
plt.show()
