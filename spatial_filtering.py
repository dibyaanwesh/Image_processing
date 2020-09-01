from PIL import Image
import numpy as np
img = Image.open('swan.png')

 
width, height = img.size

new_img= Image.new('L', (width+10,height+10))
new_img.paste(img,(5,5))


padded_arr =np.asarray(new_img)
filter_arr = np.ones((5,5))
filter_arr1= filter_arr/9
filter_arr2 = filter_arr/25


#mean filtering
def apply_filter(arr1,mask):
    img1 = arr1.copy()
    w = 2
    for i in range(5,258):
        for j in range(5,383):
            block = arr1[i-w:i+w+1, j-w:j+w+1]
            m=np.dot(block.flatten(),mask.flatten())
#             m = np.mean(block,dtype=np.float32)
            img1[i][j] = int(m)
    return img1
#arr =np.asarray(new_img)
# new_arr=padded_arr.copy()

new1_img=apply_filter(padded_arr,filter_arr1)
new2_img=apply_filter(padded_arr,filter_arr2)
img1 = Image.fromarray(new1_img)
img2 = Image.fromarray(new2_img)
img1.save("avg_img9.png")
img2.save("avg_img25.png")

 
#gaussian_filtering
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
gaussian_img.save("gaussian_img.png")
