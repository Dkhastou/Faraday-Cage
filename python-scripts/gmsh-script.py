import gmsh
import numpy as np

gmsh.initialize()

tag_counter = 1

# Function to simplify adding physical groups
def addPhysicalGroup(dimension, entity_tags, physical_group_name, list):

    global tag_counter

     # If I need to add multiple entities to one physical group, I will use a list to to do this
     # Otherwise adding physical groups is the same
    if list == 'none':
        gmsh.model.addPhysicalGroup(dim=dimension, tags=entity_tags, tag=tag_counter, name=physical_group_name)
    else:
        tags = []
        for tuple in list:
            tag = tuple[1]
            tags.append(tag)
        gmsh.model.addPhysicalGroup(dim=dimension, tags=tags, tag=tag_counter, name=physical_group_name)

    tag_counter += 1

def importModel():

    # This command opens a preexisting mesh to edit
    # gmsh.open("/home/dkhas/elmer-projects/faraday-cage-1/gmsh/mesh.msh")

    gmsh.model.add("Faraday_Cage")

    # Import CAD
    gmsh.model.occ.importShapes("../meshing/Faraday_Cage_2.step")

    # Synchronize OCC → model
    gmsh.model.occ.synchronize()

def checkMeshQuality():

    elemTypes, elemTags, elemNodeTags = gmsh.model.mesh.getElements(dim=3)

    tags = elemTags[0]

    qualities = gmsh.model.mesh.getElementQualities(elementTags=tags)
    print("Min quality:", np.min(qualities))

    if np.percentile(qualities, 1) < 0.15:
        print("Mesh rejected (1% tail too poor)")

    # if np.min(qualities) < 0.1:
    #     print("Mesh rejected")
    #     gmsh.clear()

def printInfo():

    # volumes = gmsh.model.getEntities(dim=3)
    # for dim, tag in volumes:
    #     print(f"Discrete Volume Tag: {tag}")

    # surfaces = gmsh.model.getEntities(dim=2)
    # for dim, tag in surfaces:
    #     print(f"Discrete Surface Tag: {tag}")

    # for dim, tag in gmsh.model.getEntities(3):
    #     elemTypes, elemTags, _ = gmsh.model.mesh.getElements(dim, tag)
    #     nElems = sum(len(e) for e in elemTags)
    #     print(f"Volume {tag}: {nElems} elements")

    # gmsh.model.getBoundary([(3, v)], oriented=False)

    print("Surface physical groups:", gmsh.model.getPhysicalGroups(dim=2))
    print("Volume physical groups:", gmsh.model.getPhysicalGroups(dim=3))

def definePhysicalGroups():

    # Create lists for physical groups with multiple elements
    NofluxBoundaries = []
    FloatingPotentialBoundaries = []

    # Define bounding box for surface physical groups
    xmin, ymin, zmin = 0, 0, 0
    xmax, ymax, zmax = 1, 2, 0.5


    # Define Volume physical groups
    for dim, tag in gmsh.model.getEntities(dim=3):
        volume = gmsh.model.occ.getMass(dim, tag)
        if volume > 1000000:
            addPhysicalGroup(3, [tag], "AirOutside", "none")
        elif volume < 1000000 and volume > 500000:
            addPhysicalGroup(3, [tag], "AirInside", "none")
        else:
            addPhysicalGroup(3, [tag], "Cage", "none")

    # Define Surface physical groups
    for dim, tag in gmsh.model.getEntities(dim=2):
        area = gmsh.model.occ.getMass(dim, tag)
        if area == 90000:
    
            # Set up parameterization for calculating normals
            uMin, uMax = gmsh.model.getParametrizationBounds(2, tag)
            umin, vmin = uMin
            umax, vmax = uMax

            u = 0.5 * (umin + umax)
            v = 0.5 * (vmin + vmax)

            nx, ny, nz = gmsh.model.getNormal(tag, [u, v])
                
            # Check normals. If x normal is equal to 1, this is our positive. if -1, our negative. Otherwise, we set it to airBoundary
            if nx == 1 and ny == 0 and nz == 0:
                addPhysicalGroup(2, [tag], "Positive", "none")
            elif nx == -1 and ny == 0 and nz == 0:
                addPhysicalGroup(2, [tag], "Negative", "none")
            else:
                NofluxBoundaries.append((dim, tag))

        else:
            FloatingPotentialBoundaries.append((dim, tag))

    addPhysicalGroup(2, "skip", "NofluxBoundaries", NofluxBoundaries)
    addPhysicalGroup(2, "skip", "FloatingPotentialBoundaries", FloatingPotentialBoundaries)

def createMesh():

    # Optional: Set the MSH file format version (e.g., ASCII version 2.2 for compatibility)
    gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)

    # Generate 3 dimensional mesh
    gmsh.model.mesh.generate(3)

    # Write mesh (This automatically exports it too)
    gmsh.write("../meshing/mesh.msh")

# Physical groups must be defined before meshing, because physical groups belong to the model, not the mesh.
# The mesh is generated from the model

importModel()
definePhysicalGroups()
createMesh()
checkMeshQuality()
printInfo()

gmsh.finalize()