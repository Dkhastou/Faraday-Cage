import gmsh
import inspect

# Initialize first
gmsh.initialize()

# # List all attributes under gmsh.model
# for name, obj in inspect.getmembers(gmsh.model):
#     print(name)

# # # If you want sub-modules like mesh:
# # for name, obj in inspect.getmembers(gmsh.model.mesh):
# #     print(name)

for name, obj in inspect.getmembers(gmsh.model.occ):
    print(name)

gmsh.finalize()
