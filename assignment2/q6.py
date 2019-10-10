import numpy as np
import matplotlib.pyplot as plt
import cv2

def bilateral_filtering(img,sigma_d,sigma_r,fil_size=3,padding=True,s=1):
    if padding:
        pad_size = fil_size//2
        img = np.pad(img,(pad_size,pad_size),mode='edge')

    h,w = img.shape[0],img.shape[1]
    
    rows = (h - fil_size)//s +1
    cols = (w - fil_size)//s +1
    out = np.zeros((rows,cols))
    
    
    for i in range(rows):
        for j in range(cols):
            curr = img[i:i+fil_size,j:j+fil_size]
            #calculate the filter
            r = curr.copy()
            r = np.exp((-1/(2*sigma_r*sigma_r))*(r - r[fil_size//2,fil_size//2]))
            x = np.power(np.arange(fil_size) - fil_size//2,2)
            y = x.copy().reshape(fil_size,1)
            d = np.exp(-(1/(2*sigma_d*sigma_d))*(y + x))
            fil = np.multiply(d,r)
            out[i][j] = np.sum(np.multiply(curr,fil))/np.sum(fil)
            
    return out.astype(np.uint8) 