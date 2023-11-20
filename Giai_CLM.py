import numpy as np
from PIL import Image

def logictic_map(r,x0,n):
    xn=x0
    results = []
    for i in range(n):
        xn = r*xn*(1-xn)
        results.append(xn)
    return results
def decrypt_image(encrypted_image_path,r,x0):
    image = Image.open(encrypted_image_path).convert('L')
    image_array = np.array(image)
    a,b= image.size[0],image.size[1]
    n= a*b
    key = np.array(logictic_map(r,x0,n))
    ma = key[:image_array.size].reshape(image_array.shape)
    ma = (ma*n).astype(np.uint8)
    image_array= (image_array*255).astype(np.uint8)
    decrypt_image = image_array^ ma
    decrypt_image = Image.fromarray(decrypt_image)

    return decrypt_image
image_path ='thuyvan\\qrcode.jpg'
encrypted_image_path ='thuyvan\\secret_img.jpg'
decrypt_image_path = 'thuyvan\\giai_qrcode.jpg'
r = 4
x0= 0.5
decrypt_image= decrypt_image(encrypted_image_path,r,x0)
decrypt_image.save(decrypt_image_path)
