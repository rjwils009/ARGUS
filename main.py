import pyvista as pv

# Create a 3D cube
cube = pv.Cube(
    center=(0, 0, 0,),
    x_length=2,
    y_length=2,
    z_length=2
)

# Create a desktop visualization window
plotter = pv.Plotter(
    title="Interactive 3D Viewer",
    window_size=(1000, 700)
)

# Add the cube
plotter.add_mesh(
    cube,
    color="royal_blue",
    show_edges=True,
    edge_color="black",
    smooth_shading=True
)

# Add reference axes and a grid
plotter.add_axes()
plotter.show_grid()

# Set the starting camera position
plotter.camera_position = "iso"

# open the interactice window
plotter.show()