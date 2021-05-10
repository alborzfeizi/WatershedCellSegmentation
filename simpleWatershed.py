#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.feature import peak_local_max
from skimage.morphology import watershed
from skimage import color
from scipy import ndimage
import numpy as np
import imutils
import cv2

################################ script inputs ##############################
threshold_percent = 5; # used to remove background noise
denoise_value = 10; # used for the open morphological operation
min_distance_value = 10; # used for finding local minima (watershed seed)
#############################################################################

# In[2]:

# load the image
image = cv2.imread('sampleImages/A02_Bottom Slide_R_p01_0_A01f10d2.TIF', cv2.IMREAD_ANYDEPTH)
image = (image/4095)*255
image = np.uint8(image)
# image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)


# In[3]:

#%matplotlib auto
cv2.imshow("Input", image)
cv2.waitKey(0) 

# In[4]:


thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
thresh2 = cv2.threshold(image, threshold_percent*2.55, 255, cv2.THRESH_BINARY)[1]
thresh = thresh & thresh2;

# Denoise

arr_size = denoise_value;
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (arr_size, arr_size))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cv2.imshow("Thresh", thresh)
cv2.waitKey(0) 


# In[5]:


D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=min_distance_value, labels=thresh)


# In[10]:


markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)
img2 = color.label2rgb(labels, bg_label=0)
# fig=plt.figure()
# plt.imshow(img2, cmap='jet')
cv2.imshow("color", img2)
cv2.waitKey(0) 

# In[ ]:


# loop over the unique labels returned by the Watershed
# algorithm
for label in np.unique(labels):
	# if the label is zero, we are examining the 'background'
	# so simply ignore it
	if label == 0:
		continue
	# otherwise, allocate memory for the label region and draw
	# it on the mask
	mask = np.zeros(image.shape, dtype="uint8")
	mask[labels == label] = 255
	# detect contours in the mask and grab the largest one
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv2.contourArea)
	# draw a circle enclosing the object
	((x, y), r) = cv2.minEnclosingCircle(c)
	cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
	cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


# In[9]:


# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
count_output = np.max(labels);
print("Total number of cells detected: ", count_output);

# In[10]:
    
# save the output image
cv2.imwrite('labeled_grayscale.png', image)
cv2.imwrite('watershed_labels.png', np.uint8(img2*255))