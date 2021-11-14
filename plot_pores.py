import numpy as np
import pyvista as pv

#Load data
pts = np.load("pores_cloud.npy", allow_pickle = True)
A   = np.load("volume.npy", allow_pickle = True)

#Wrap arrays as volume and point cloud
data = pv.wrap(A)
point_cloud = pv.PolyData(pts)

#Visualise using pvyista - overlay ct scan with pores
p = pv.Plotter(notebook=False)
p.add_volume(data, opacity=2, shade=False, cmap="bone")
p.add_mesh(point_cloud, color='maroon', point_size=4,render_points_as_spheres=True)
p.show()


