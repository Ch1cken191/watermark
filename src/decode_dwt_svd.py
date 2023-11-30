import cv2
import numpy as np
import pywt

cover_img = cv2.imread('image//re_1_cover.png',0)
coeffs = pywt.dwt2(cover_img,'haar')
cA,(cH,cV,cD) = coeffs

def mang(cover):
    U,s,V = np.linalg.svd(cover)
    secret_cA = np.zeros_like(cover)
    alpha = 0.9
    for i in range(len(cover)):
        mau = U[i,:10]*s[:10]@V[:10,:]
        for j in range(len(cover[0])):
            if (i<len(secret_cA) and len(secret_cA[0])):
                secret_cA[i][j] = (cover[i][j] - mau[j]*alpha)*(1-alpha)
    return secret_cA

secret_img = cv2.imread("image//en_QR_Image.png",0)
secret_coeffs = pywt.dwt2(secret_img,'haar')
secret_cA,(secret_cH,secret_cV,secret_cD) = secret_coeffs
new_shape = (200,200)

new_array = np.zeros(new_shape)
new_array[:new_array.shape[0],:new_array.shape[1]]= mang(cA)[:new_array.shape[0],:new_array.shape[1]]
secret_coeffs = new_array,(secret_cH,secret_cV,secret_cD)

secret_img_new = pywt.idwt2(secret_coeffs,"haar")
cv2.imwrite("image//extracted_QR.png",secret_img_new)
