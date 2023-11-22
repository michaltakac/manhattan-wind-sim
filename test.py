
import numpy as np
from modulus.sym.geometry.tesselation import Tessellation
from modulus.sym.utils.io.vtk import var_to_polyvtk

# number of points to sample
nr_points = 100000

geo = Tessellation.from_stl("./box_open_manhattan.stl")

# sample geometry for plotting in Paraview
s = geo.sample_boundary(nr_points=nr_points)
var_to_polyvtk(s, "boundary")
print("Surface Area:{:.3f}".format(np.sum(s["area"])))
s = geo.sample_interior(nr_points=nr_points, compute_sdf_derivatives=True)
var_to_polyvtk(s, "interior")
print("Volume:{:.3f}".format(np.sum(s["area"])))