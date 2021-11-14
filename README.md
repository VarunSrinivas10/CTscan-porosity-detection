# CTscan-Porosity-detection
This repository contains OpenCV and PyVista based code to detect and visualise defects/pores in 3D CT scans of components. 3D CT scans usually return a number of depth-wise 2D images of the component made after sectioning either laterally or vertically. Pores are usually seen as discolorations. I have used the simple blob detector from opencv to detect the pores, store their centers in an array and use pyvista to overlay the CT scan images into 3D along with plotting the locations of the pores as a point cloud.

### Requirements:
OpenCV, PyVista, Pillow and Numpy 

### To run:
  1. Enter the path to the Folder containing the images in the parameters.txt file
  2. On the next line, enter the name of the images. For example, if your images are labeled image1, image2 and so on, enter - image
  3. Enter the range of numbering in the next line. For example, if your images are named image1, image2 ... image300 then enter - 1 300
  4. Usually, it is advisable to have OpenCV and PyVista in different environments to avoid conflicts
  5. First execute the detect_pores.py file and subsequently plot_pores.py in the respective environments. detect_pores requires OpenCV and plot_pores needs PyVista

### Output:
If executed from the command line, a window pops up with the visualisation. For further analysis on the pores, the locations of the pores is stored as an npy file.
