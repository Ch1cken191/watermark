import cv2
import numpy as np
import pywt

secret_img = cv2.imread("thuyvan\\ma_qrcode.png",0)
cover_img = cv2.imread("thuyvan\\lonbadoi.jpg")

coeffs = pywt.dwt2(cover_img,"haar")
cA,(cH,cV,cD)= coeffs
U,s,V= np.linalg.svd(cA)


secret_coeffs = pywt.dwt2(secret_img,'haar')
secret_cA ,(secret_cH,secret_cV,secret_cD) =secret_coeffs
def mang(cover,secret):
    U,s,V = np.linalg.svd(cover)
    alpha = 0.03
    cA_new = list()
    for i in range(len(cover)):
        cA_1 = []
        for j in range(len(cover[0])):
            if (i < len(secret) and j<len(secret[0])):
                test = cover[i][j] + alpha* secret[i][j]
            else:
                test = cover[i][j] + alpha
            cA_1.append(test)
        cA_new.append(cA_1)
    return cA_new
s[:10] = 0
cA_new = mang(cH,secret_cH)
cH_new = mang(cH,secret=secret_cH)
cV_new = mang(cV,secret=secret_cV)
cD_new = mang(cD,secret=secret_cD)
coeffs_new = cA_new,(cH_new,cV_new,cD_new)

img_new = pywt.idwt2(coeffs_new,"haar")
cv2.imwrite('thuyvan\\an_ma.jpg',img_new)
