# SP24_V313_P01_SzymanskiGracie_maya_particles_v01
# Runs a program that creates files that include shape particle points
# By Gracie Szymanski
# Created 3/29/24 Modified 5/3/24

import SP24_V313_P01_SzymanskiGracie_gen_coords_v02 as gc
import os

#Constants
EXT = "py" #File type
EXT2 = "mel" #File type

#A function that writes out the different file types
def file_type_conditional(file_type, file_name, shape_points, path):

    if file_type == "Python":
        
        outfile_name = f"{os.path.join(path, file_name)}.{EXT}" #Creates file name
        
        with open(outfile_name, "w") as file:  # Open the file for writing

            # Write the first 3 lines
            file.write("import maya.cmds as cmds\n\ncmds.nParticle(p=[\n")

            # Loop thru all the geometry points & write them out
            for x,y,z in shape_points:
                file.write(f"({x}, {y}, {z}),\n")

            # Write the last line of the file
            file.write(f"], n = '{file_name}')\n")

        print ("Done Writing File!")

    if file_type == "MEL":

        outfile_name = f"{os.path.join(path, file_name)}.{EXT2}" #Creates file name

        with open(outfile_name, "w") as file:  # Open the file for writing
            
            #Writes the first line of code
            file.write("nParticle\n")

            #Loops thru all the geometry points and writes them
            for x,y,z in shape_points:
                file.write(f"-p {x} {y} {z} \n")

        print ("Done Writing File!")


#A function to write a file that shows point coordinates inside a cube
def write_cube(file_name, count, size, file_type, path, cx, cy, cz):
    shape_points = gc.make_cube(count, size, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)
    

#A function to write a file that shows point coordinates inside a hollow cube
def write_hol_cube(file_name, count, size, hollow_size, file_type, path, cx, cy, cz):

    shape_points = gc.make_hol_cube(count, size, hollow_size, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a sphere
def write_sphere(file_name, count, diameter, file_type, path, cx, cy, cz):
    shape_points = gc.make_sphere(count, diameter, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a hollow sphere
def write_hol_sphere(file_name, count, hollow_diameter, diameter, file_type, path, cx, cy, cz):

    shape_points = gc.make_hol_sphere(count, hollow_diameter, diameter, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a cylinder
def write_cylinder(file_name, count, diameter, height, file_type, path, cx, cy, cz):
    
    shape_points = gc.make_cylinder(count, diameter, height, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a disk
def write_disk(file_name, count, diameter, file_type, path, cx, cy, cz):
    
    shape_points = gc.make_disk(count, diameter, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a cone
def write_cone(file_name, count, diameter, height, file_type, path, cx, cy, cz):
    
    shape_points = gc.make_cone(count, diameter, height, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a diamond
def write_diamond(file_name, count, size, file_type, path, cx, cy, cz):
    
    shape_points = gc.make_diamond(count, size, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a heart shape
def write_heart(file_name, count, size, thickness, file_type, path, cx, cy, cz):
    
    shape_points = gc.make_heart(count, size, thickness, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)


#A function to write a file that shows point coordinates inside a heart shape
def write_pyramid(file_name, count, size, height, file_type, path, cx, cy, cz):

    shape_points = gc.make_pyramid(count, size, height, cx, cy, cz)  # Generates geometry points from gen_coords file
    file_type_conditional(file_type, file_name, shape_points, path)
