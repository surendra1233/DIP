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
    out = np.zeros((rows,cols,3))
    
    
    for i in range(rows):
        for j in range(cols):
            curr = img[i:i+fil_size,j:j+fil_size]
            #calculate the filter
            r = curr.copy()
            r = np.exp((-1/(2*sigma_r*sigma_r))*(r - r[fil_size//2,fil_size//2,:]))
            
            x = np.power(np.arange(fil_size) - fil_size//2,2)
            y = x.copy().reshape(fil_size,1)
            d = np.zeros(r.shape)
            d[:,:,0] = d[:,:,1] = d[:,:,2] = np.exp(-(1/(2*sigma_d*sigma_d))*(y + x))
            
            fil = np.multiply(d,r)
            
            temp = np.multiply(curr,fil)
            out[i,j,0] = np.sum(temp[:,:,0])/np.sum(fil)
            out[i,j,1] = np.sum(temp[:,:,1])/np.sum(fil)
            out[i,j,2] = np.sum(temp[:,:,2])/np.sum(fil)
            
    return out.astype(np.uint8) 

img = cv2.imread('./sky.png')
gt = cv2.imread('./gt_sky.png')
a = np.ones((200,1))

for i in range(1,201):
    x=y=i
    out = bilateral_filtering(img,x,y)
    a[i-1] = np.sum(np.power(out-gt,2))

print(np.argmin(a)+1)