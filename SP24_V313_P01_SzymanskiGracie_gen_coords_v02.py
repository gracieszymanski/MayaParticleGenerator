# SP24_V313_P01_SzymanskiGracie_gen_coords_v01
# Generates that coordinates used in Maya Particles File
# By Gracie Szymanski
# Created 3/29/24 Modified 5/3/24

import random as rnd
import math as math


#A function to generate random points within a cube
def make_cube(count, size, cx, cy, cz):

    points = [] #Creates an empty list

    for pt in range(count): #generates random points within the cube
        x = rnd.uniform(-size/2, size/2)
        y = rnd.uniform(-size/2, size/2)
        z = rnd.uniform(-size/2, size/2)

        #edits points to conform to user inputted center
        x = x + cx
        y = y + cy
        z = z + cz
        points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random points within a hollow cube
def make_hol_cube(count, size, hollow_size, cx, cy, cz):
    
    points = [] #Creates an empty list

    while len(points) < count: 
        #Generates random points within a cube
        x = rnd.uniform(-size/2 , size/2)
        y = rnd.uniform(-size/2, size/2)
        z = rnd.uniform(-size/2, size/2)

        #A math formula that throws away any points that are not within the cube's thickness
        if abs(x) > hollow_size/2 or abs(y) > hollow_size/2 or abs(z) > hollow_size/2:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random points within a sphere
def make_sphere(count, diameter, cx, cy, cz):

    points = [] #Creates an empty list
    radius = diameter/2 #Defines the radius of the sphere

    while len(points) < count:
        #Generates random points within a cube to act as bounding box
        x = rnd.uniform(-radius, radius)
        y = rnd.uniform(-radius, radius)
        z = rnd.uniform(-radius, radius)
        
        #The distance from the origin to the random point is calculated
        distance = math.sqrt(x**2 + y**2 + z**2)

        #If the point is farther than the length of the radius, it is thrown out
        if radius >= distance:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random points within a hollow sphere
def make_hol_sphere(count, hollow_diameter, diameter, cx, cy, cz):

    points = [] #Creates an empty list
    radius_outer = diameter/2 #Defines te radius of the outer circle
    radius_inner = hollow_diameter/2 #Defines the radius of the hollow inner circle

    while len(points) < count:
        #Generates random points withing a cube to act as a bouning box
        x = rnd.uniform(-radius_outer, radius_outer)
        y = rnd.uniform(-radius_outer, radius_outer)
        z = rnd.uniform(-radius_outer, radius_outer)
        
        #The distance from the origin to the random point is calculated
        distance = math.sqrt(x**2 + y**2 + z**2)

        #A math function to determine if the point is within the large sphere but larger than the hollow sphere
        #If the point is not within the thickness, it is thrown out
        if radius_outer >= distance >= radius_inner:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list
    
    return points


#A function to generate random points within a cylinder
def make_cylinder(count, diameter, height, cx, cy, cz):

    points = [] #Creates and empty list
    radius = diameter/2 #Defines the radius of the base of the cylinder

    while len(points) < count:
        #Generates random points in a rectangle to act as a bounding box
        x = rnd.uniform(-radius, radius)
        y = rnd.uniform(-height/2, height/2)
        z = rnd.uniform(-radius, radius)

        #The distance from the origin to the (x,z) point is calculated
        distance = math.sqrt(x**2 + z**2)

        #If the radius of the base circle is larger than the (x,z) point distance then the point is thrown out
        if radius >= distance:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random points within a flat disk
def make_disk (count, diameter, cx, cy, cz):

    points = [] #Creates and empty list
    radius = diameter/2 #Calculates the radius of the disk

    while len(points) < count:
        #Generates random points in a flat square to use as a bounding box
        x = rnd.uniform(-radius, radius)
        y = 0
        z = rnd.uniform(-radius, radius)

        #The distance from the origin to the (x,z) point is calculated
        distance = math.sqrt(x**2 + z**2)

        #If the distance of the (x, z) point to the origin is larger than the radius, it is thrown out
        if radius >= distance:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random points in a cone
def make_cone(count, diameter, height, cx, cy, cz):

    points = [] #Creates an empty list
    radius = diameter/2 #Calculates the radius of the base of the cone

    while len(points) < count:
        #Generates random points in a rectangle to act as a bounding box
        x = rnd.uniform(-radius, radius)
        y = rnd.uniform(0, height)
        z = rnd.uniform(-radius, radius)
        
        #The distance from the origin to the (x,z) point is calculated
        distance = math.sqrt(x**2 + z**2)

        #A math formula to calculate the radius of the cone at a specific point
        #If the distance of the (x,z) point is larger than the radius at that y point, it is thrown out
        if radius * (1- y / height) >= distance: 
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list
            
    return points


#A function to generate random points in a diamond shape
def make_diamond(count, size, cx, cy, cz):

    points = [] #Creates an empty list

    while len(points) < count:
        #Generates random points in a cube to act as a boundint box
        x = rnd.uniform(-size/2, size/2)
        y = rnd.uniform(-size/2, size/2)
        z = rnd.uniform(-size/2, size/2)

        #If the point does not lie within the diamond, it is thrown out
        #Used triangles in the math to calculate diamond positions
        if abs(x) + abs(y) + abs(z) <= size/2:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points


#A function to generate random  points in a heart shape
def make_heart(count, size, thickness, cx, cy, cz):
    
    points = [] #Creates an empty list

    while len(points) < count:
        #A loop that generates the points inside the bottom triangle of the heart
        for i in range(17): #Inside a for loop so that the amount of particles in the whole heart are evenly placed
            #Generates random points inside a standing square to act as a bounding box
            x = rnd.uniform(-size/2, size/2)
            y = rnd.uniform(-size, 0)
            z = rnd.uniform(-thickness/2, thickness/2)

            #If the points are outside the triangular shape, they are thrown out
            if abs(x) + abs(y) <= size/2 and len(points)< count:
                #edits points to conform to user inputted center
                x = x + cx
                y = y + cy
                z = z + cz
                points.append((x, y, z)) #makes coordinates into a tuple and appends to list
        

        #After the loop runs
        #These lines of code generate the first semi circle top of heart
        radius = size/4.3 #Calculates the radius of the semi circles

        #Generates random points in a standing rectangle to act as a bounding box
        x = rnd.uniform(-radius, radius)
        y = rnd.uniform(radius/8, radius)
        z = rnd.uniform(-thickness/2, thickness/2)
        
        #The distance from the origin to the random point is calculated
        distance = math.sqrt(x**2 + y**2) 

        #If the point is outside the semi circle's radius, it is thrown out
        if radius >= distance and len(points)< count:
            x = x - size/4.3 #The point is then moved to the left to create the heart shape
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list
        

        #These lines of code generate the first semi circle top of heart
        #Generates random points in a standing rectangle to act as a bounding box
        x = rnd.uniform(-radius, radius)
        y = rnd.uniform(radius/8, radius)
        z = rnd.uniform(-thickness/2, thickness/2)

        #The distance from the origin to the random point is calculated
        distance = math.sqrt(x**2 + y**2)

        #If the point is outside the semi circle's radius, it is thrown out
        if radius >= distance and len(points)< count:
            x = x + size/4.3 #The point is then moved to the right to create the heart shape
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points

def make_pyramid(count, size, height, cx, cy, cz):
        
    points = []  #Creates an empty list
    size = size / 2  #Calculates the size of the base of the pyramid

    while len(points) < count:
        #Generates random points within a rectangle to act as a bounding box
        x = rnd.uniform(-size, size)
        y = rnd.uniform(0, height)
        z = rnd.uniform(-size, size)
        
        #checks if the point is within the pyramid shape
        if abs(x) / size + abs(z) / size <= 1 - y / height:
            #edits points to conform to user inputted center
            x = x + cx
            y = y + cy
            z = z + cz
            points.append((x, y, z)) #makes coordinates into a tuple and appends to list

    return points
