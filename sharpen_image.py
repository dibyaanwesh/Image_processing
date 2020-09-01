from PIL import ImageChops
from PIL import Image
import numpy as np


img=Image.open('swan.png', 'r').convert('L')
#gaussian_filtering
width, height = img.size

new_img= Image.new('L', (width+10,height+10))
new_img.paste(img,(5,5))


padded_arr =np.asarray(new_img)



gauss_filter=np.array([1,4,7,4,1,4,16,26,16,4,7,26,41,26,7,4,16,26,16,4,1,4,7,4,1])
gauss_filter=gauss_filter/273
gauss_filter.shape=(5,5)

def GaussFilter(arr,filterr):
    img1 = arr.copy()
    w = 2
    for i in range(5,258):
        for j in range(5,383):
            block = arr[i-w:i+w+1, j-w:j+w+1]
            m=np.dot(block.flatten(),filterr.flatten())
            img1[i][j] = int(m)
    return img1


gaussFilterImg=GaussFilter(padded_arr, gauss_filter)
gaussian_img= Image.fromarray(gaussFilterImg)



#real part starts here
unsharp_mask=ImageChops.subtract(new_img,gaussian_img)

#add_mask
mask_org=ImageChops.add(new_img,unsharp_mask)
 
weight=2
weighted_Mask=unsharp_mask.point(lambda i:weight*i)
 
#highboosting
highBoostFilterImg=ImageChops.add(new_img,weighted_Mask)
highBoostFilterImg.save("highboost_filtered.png")
