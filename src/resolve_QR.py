import numpy as np
from PIL import Image

# Hàm sử dụng phương trình ánh xạ logistic 
# để tạo ra một mảng các số ngẫu nhiên
def logistic_map(r,x0,n):
    xn = x0
    resutls = []
    for i in range(n):
        xn = r*xn*(1-xn)
        resutls.append(xn)
    return resutls

# Hàm mã hóa ảnh
def encrypt_image(image_path,r,x0):
# Tính toán giá trị của phương trình ánh xạ logistic
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    a,b = image.size[0],image.size[1]
    n= a*b
    key = np.array(logistic_map(r,x0,n))
    
# Trích xuất các bit của ảnh = ảnh QR
# sau đó XOR với mảng key (logistic map)
# Được ảnh mã hóa
    ma = key[:image_array.size].reshape(image_array.shape)
    ma = (ma*n).astype(np.uint8)
    image_array = (image_array*255).astype(np.uint8)
    encrypt_image = image_array ^ ma
    encrypt_image = Image.fromarray(encrypt_image)
    return encrypt_image

image_path = 'image\\QR_Image.jpg'
encrypt_image_path = 'image\\en_QR_Image.png'
r= 4
x0= 0.5
encrypt_image = encrypt_image(image_path,r,x0)
encrypt_image.save(encrypt_image_path)



