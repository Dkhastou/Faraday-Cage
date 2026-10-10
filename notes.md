

------- NOTES ON ORGANIZATION AND DIRECTORY STRUCTURE -------

This Template can be copied to start any Elmer project.

The 'results', and 'mesh' directories are not included in the template as they will
be generated during the process of building the mesh and running the solver

All .sif files should be kept in the sif folder for organization.

------ NOTES ON .sif FILES ------

Notes on how to interpret the .sif language (most of which comes from fortran) are located in the sif directory.
If there is confusion at any point in how the declarations for certain parts of the code should work, reference 
these notes  

------ NOTES FOR USING AND LEARNING ELMER ------

1. Download CAD Model as .step file, and copy it into the project directory
2. in the mesh.geo script, use "Merge" to import the CAD model for meshing, and then script out the commands that must be used to turn
the CAD model into a mesh. Define physical groups, both volume and surfaces. Save everything. 
3. Open the mesh.geo file in gmsh, and check that the desired outcome is correct using the viewer
4. Export the .geo file as a .msh file into the project directory
5. use ElmerGrid to turn the .msh file into a mesh directory that Elmer can read

When using ElmerSolver, you do not need to delete the results directory everytime you want to rerun the solver
ElmerSolver should rewrite the results directory for you without needing to manually delete it.

------ USEFUL COMMANDS ------

	gmsh mesh.geo -3 -format msh2
	gmsh mesh.geo -3 -format msh2 > gmsh-output.log && grep "Warning" gmsh-output.log && gmsh mesh.msh

The above command will turn a .geo file into the necessary .msh file, and is generally better than
trying to export using gmshs GUI. The second command puts the output into a log file and displays errors, which makes
debugging the .geo file much easier. 

	nm -D /usr/local/share/elmersolver/lib/HeatSolve.so | grep -i solver

The above command lists all subroutines for a solver. Usually there is only one correct one to use in the .sif file,
and it is the least verbose result. The nm commands lists symbols from object files and binaries, in this case the 
.so file extension (Stands for shared object). Primarily used when dealing with compiled code such as Fortran, C, C++, etc.

------ EXAMPLE PROJECT LOCATIONS ------

Examples are located in this folder: (NOT THE EXAMPLES FOLDER, the tests folder)
/mnt/c/Users/dkhas/elmerfem/fem/tests

------ PRINTING ELMERSOLVER TO .log FILE ------

	ElmerSolver > output.log

This prints The ElmerSolver log into the output.log file instead of just printing to the terminal
Incredibely useful for looking at results much later using a command like grep

------ LOOK UP KEY WORDS FOR ANY SOLVER ------

	grep -e "GetInteger(" -e "GetString(" -e "GetReal(" /mnt/c/Users/dkhas/elmerfem/fem/src/modules/StatElecSolve.F90

The -e flag tells grep to look for all strings at once
Change the solver to whatever solver I need to find keywords for


