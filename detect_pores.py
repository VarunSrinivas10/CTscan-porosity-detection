import cv2
import numpy as np
import math

#List for defect locations
A = []

#Read parameters
f    = open("parameters.txt", "r")
path = f.readline().strip()
name = f.readline().strip()
rnge = f.readline().strip().split()
ext  = f.readline().strip()

rngmin = int(rnge[0])
rngmax = int(rnge[1]) + 1

#Get image size
filename = path+name+str(rngmin).zfill(3)+"."+ext
img      = cv2.imread(filename, 0)
img2     = np.asarray(img)
shape    = img2.shape
x2       = shape[0]
x1       = shape[1]

#delete
del img,img2,shape

#Array to stack images to form 3D representation
B = np.zeros((rngmax,x1,x2))

#Blob Params
blob_params = cv2.SimpleBlobDetector_Params()
blob_params.minDistBetweenBlobs = 1
blob_params.filterByArea = True
blob_params.minArea = 8

#Detect pores
for i in range(rngmin, rngmax):
	filename = path+name+str(i).zfill(3)+"."+ext
	print(filename)
	
	#Import Image
	gray = cv2.imread(filename, 0)

	#Sharpen
	kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	im = cv2.filter2D(gray, -1, kernel)

	#Blob Detector
	detector = cv2.SimpleBlobDetector_create(blob_params)
	keypoints = detector.detect(im)

	#Save Keypoint
	for keyPoint in keypoints:
		x = keyPoint.pt[0]
		y = keyPoint.pt[1]
		A.append([i,x,y])

	#Save volume
	B[i] = np.asarray(gray).transpose()

C = np.asarray(A)
np.save("pores_cloud",C)
np.save("volume",B)





