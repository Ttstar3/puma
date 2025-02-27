import numpy as np
import pumapy as puma
import pyvista as pv
import os

# The objective of this notebook is to familiarize new users with the main datastructures that stand at the basis of the
# PuMA project, and outline the functions to compute material properties (please refer to these papers
# ([1](https://www.sciencedirect.com/science/article/pii/S2352711018300281),
# [2](https://www.sciencedirect.com/science/article/pii/S235271102100090X)) for more details on the software).

notebook = False  # when running locally, actually open pyvista window
export_path = "out"  # CHANGE THIS PATH
if not os.path.exists(export_path):
    os.makedirs(export_path)


# ## Tutorial
# 
# In this section, we discuss how to automatically detect the orientation in a raw grayscale micro-CT image.
# In the PuMA C++ library, there are three different algorithms to detect it: the artificial flux, the ray casting
# approach, and the structure tensor. Each one of these methods has its pros and cons, but latter one is widely considered
# the state-of-the-art for detecting the local orientation directly from the raw image grayscales (please refer to
# [this paper](https://www.sciencedirect.com/science/article/abs/pii/S0927025620301221) for more details on the three
# PuMA methods). For this reason, the structure tensor method was implemented in pumapy, using Numpy's vectorized eigen
# value analysis routines.
# 
# The structure tensor is an image processing approach that directly operates on the grayscale values of a 3D image.
# Effectively, what the algorithm looks for is the direction of least grayscale gradient change at each voxel throughout
# the domain. It does so by applying a Derivative of Gaussian (DoG) filter, followed by an extra Gaussian smoothing of the gradients.
# 
# The pumapy function to compute the orientation can be used in the following way:

size = (100, 100, 100)  # size of the domain, in voxels. 
radius = 6  # radius of the fibers to be generated, in voxels
nFibers = None  # Can specify either the number of fibers or the porosity
porosity = 0.8  # porosity of the overall structure
phi = 90    # A value between 0 and 90 that controls the amount that the fibers lie *out of* the XY plane,
            # with 0 meaning all fibers lie in the XY plane, and 90 meaning that cylinders are randomly oriented out of the
            # plane by as much as +/- 90 degrees.
theta = 90  # A value between 0 and 90 that controls the amount of rotation *in the* XY plane,
            # with 0 meaning all fibers point in the X-direction, and 90 meaning they are randomly rotated about the
            # Z axis by as much as +/- 90 degrees.
length = 100 # Length of the fibers to be generated
max_iter = 3  # optional (default=3), iterations to refine the porosity
allow_intersect = True  # optional (default=True), allow intersection betweem the fibers: if equal to False, the function runs considerably more slowly because    
                        # randomly proposed fibers are rejected if they intersect any other fiber - use with relatively high porosity for reasonable runtimes 
segmented = False  # assign unique IDs to each fiber (if set to False, range will be from 0-255)

ws_fibers = puma.generate_random_fibers(size, radius, nFibers, porosity, phi, theta, length, allow_intersect=allow_intersect, segmented=segmented)

# sigma is the std of the DoG, whereas rho is the one of the second Gaussian smoothing
# in order to obtain optimal performance, we should always have:  sigma > rho
puma.compute_orientation_st(ws_fibers, cutoff=(128, 255), sigma=1.4, rho=0.7)

# The orientation field is automatically added to the workspace.orientation Numpy array. We can now visualize it by running: 


p = pv.Plotter(shape=(1, 2), notebook=notebook)
p.subplot(0, 0)
p.add_text("Microstructure")
puma.render_contour(ws_fibers, (128, 255), notebook=notebook, add_to_plot=p, plot_directly=False)
p.subplot(0, 1)
p.add_text("Detected fiber orientation")
puma.render_orientation(ws_fibers, notebook=notebook, add_to_plot=p, plot_directly=False)
p.show()

# The local material orientation is an important input to the functions to compute the effective conductivity and elasticity,
# when treating the local phases as anisotropic.

# ### Orientation Detection on Segmented Images
# 
# For segmented images, the orientation detection requires a pre-processing step to apply a Euclidean Distance Transform
# prior to running the structure tensor. This pre-processing is an optional step in the oritention module, and can be
# activated by setting the edt=True flag. An example is shown below for a segmented random fiber structure

size = (100, 100, 100)  # size of the domain, in voxels. 
radius = 6  # radius of the fibers to be generated, in voxels
nFibers = None  # Can specify either the number of fibers or the porosity
porosity = 0.8  # porosity of the overall structure
phi = 90    # A value between 0 and 90 that controls the amount that the fibers lie *out of* the XY plane,
            # with 0 meaning all fibers lie in the XY plane, and 90 meaning that cylinders are randomly oriented out of the
            # plane by as much as +/- 90 degrees.
theta = 90  # A value between 0 and 90 that controls the amount of rotation *in the* XY plane,
            # with 0 meaning all fibers point in the X-direction, and 90 meaning they are randomly rotated about the
            # Z axis by as much as +/- 90 degrees.
length = 100 # Length of the fibers to be generated
max_iter = 3  # optional (default=3), iterations to refine the porosity
allow_intersect = True  # optional (default=True), allow intersection betweem the fibers: if equal to False, the function runs considerably more slowly because    
                        # randomly proposed fibers are rejected if they intersect any other fiber - use with relatively high porosity for reasonable runtimes 
segmented = True  # assign unique IDs to each fiber (if set to False, range will be from 0-255)

ws_fibers = puma.generate_random_fibers(size, radius, nFibers, porosity, phi, theta, length, allow_intersect=allow_intersect, segmented=segmented)

# sigma is the std of the DoG, whereas rho is the one of the second Gaussian smoothing
# in order to obtain optimal performance, we should always have:  sigma > rho
puma.compute_orientation_st(ws_fibers, cutoff=(1, 49), sigma=1.4, rho=0.7, edt=True)

# The orientation field is automatically added to the workspace.orientation Numpy array. We can now visualize it by running:

p = pv.Plotter(shape=(1, 2), notebook=notebook)
p.subplot(0, 0)
p.add_text("Microstructure")
puma.render_contour(ws_fibers, (1, 49), notebook=notebook, add_to_plot=p, plot_directly=False)
p.subplot(0, 1)
p.add_text("Detected fiber orientation")
puma.render_orientation(ws_fibers, notebook=notebook, add_to_plot=p, plot_directly=False)
p.show()

