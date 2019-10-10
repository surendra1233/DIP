import numpy as np
import cv2
from matplotlib import pyplot as plt

def dist(a,b):
    f = np.array([1,1,1])
    a = np.dot(np.power(a-b,2),f)
    return np.power(a,1/2)

fg = cv2.imread('./DIP_2019_A1/fg.jpg')
bg = cv2.imread('./DIP_2019_A1/bg.jpg')

ggreen = np.array([0,255,0])
dist_mat = dist(fg,green)
bin_mat = dist_mat > 100
out = bg
out[bin_mat,:] = fg[bin_mat,:]
plt.imshow(out)
plt.show()
