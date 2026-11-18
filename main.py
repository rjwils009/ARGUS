import pyvista as pv

pv.set_jupyter_backend("client")

# Available 3D objects
objects = {
    "Cube": pv.Cube(
        center=(0, 0, 0),
        x_length=2,
        y_length=2,
        z_length=2
    ),
    "Sphere": pv.Sphere(
        radius=1,
        theta_resolution=48,
        phi_resolution=48
    ),
    "Cylinder": pv.Cylinder(
        radius=1,
        height=2
    ),
    "Cone": pv.Cone(
        height=2,
        radius=1
    ),
    "Torus": pv.ParametricTorus()
}

# Select an Object
selected_object = "Cube"

# Create browser viewer
plotter = pv.Plotter(
    notebook=True,
    window_size=(1000, 700)
)

plotter.set_background("#1e1e1e")

plotter.add_mesh(
    objects[selected_object],
    color="royalblue",
    show_edges=True,
    edge_color="black",
    smooth_shading=True
)

plotter.add_axes()
plotter.show_grid()
plotter.camera_postition = "iso"

#display interative scene
plotter.show(jupyter_backend="client")