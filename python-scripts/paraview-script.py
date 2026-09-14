from paraview.simple import *

# Load a dataset
data = OpenDataFile("Z:/home/dkhas/elmer-projects/faraday-cage-1/results/results-vtu/case_t0001.vtu")

# # Apply a contour filter
# contour = Contour(Input=data)
# contour.ContourBy = ['POINTS', 'Pressure']
# contour.Isosurfaces = [101325]

# # Show in active view
# Show(contour)
# Render()

