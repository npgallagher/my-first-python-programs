#This program contains functions that evaluate formulas used in geometry.
#
#Noah Gallagher
#August 30, 2017

print ("Program options:")
print ("-triangle_area, base and height")
print ("-circle_area, radius")
print ("-parallelogram_area, base and height")
print ("-trapezoid_area, base, base, height")
print ("-rectangular_prism_volume, width height and length")
print ("-cone_volume, radius and height")
print ("-rectangular_prism_surface_area, length width and height")
print ("-surface_area_sphere, radius")
print ("-hypotenuse_right_triangle, a length and b length")
print (" ")


import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(b, c, h):
    a = ((b+c)/2) * h
    return a

def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v

def rectangular_prism_surface_area(l, w, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def surface_area_sphere(r):
    a = 4 * math.pi * r**2
    return a

def hypotenuse_right_triangle(a, b):
    c = (a ** 2 + b ** 2) ** .5
    return c

