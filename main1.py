from sys import argv
import math
script, x = argv
x=int(x)
if x <= 6:
    y = x + x ** 0.5
else:
    y = x * x ** 0.5
print("y=",y)
