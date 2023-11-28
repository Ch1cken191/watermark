import cv2
import numpy as np
import pywt

def giai_ma(cA, secret):
    U, s, V = np.linalg.svd(cA)
    alpha = 0.03
    cA_decoded = np.zeros_like(cA)
    for i in range(len(cA)):
        for j in range(len(cA[0])):
            if (i < len(secret) and j < len(secret[0])):
                cA_decoded[i][j] = (cA[i][j] - alpha * secret[i][j]) / (1 - alpha)
            else:
                cA_decoded[i][j] = cA[i][j] / (1 - alpha)
    return cA_decoded

def giai_ma_va_luu(cover, secret, output_path):
    # Áp dụng DWT để trích xuất các thành phần cA, cH, cV, cD
    coeffs_cover = pywt.dwt2(cover, 'haar')
    cA_cover, (cH_cover, cV_cover, cD_cover) = coeffs_cover

    # Áp dụng DWT để trích xuất các thành phần cA, cH, cV, cD
    coeffs_secret = pywt.dwt2(secret, 'haar')
    cA_secret, (cH_secret, cV_secret, cD_secret) = coeffs_secret

    # Giải mã từng thành phần
    cA_decoded = giai_ma(cA_cover, cA_secret)
    cH_decoded = giai_ma(cH_cover, cH_secret)
    cV_decoded = giai_ma(cV_cover, cV_secret)
    cD_decoded = giai_ma(cD_cover, cD_secret)

    # Tạo các thành phần mới
    coeffs_decoded = cA_decoded, (cH_decoded, cV_decoded, cD_decoded)

    # Tái tạo ảnh gốc
    img_decoded = pywt.idwt2(coeffs_decoded, 'haar')

    # Lưu ảnh giải mã
    cv2.imwrite(output_path, img_decoded)

    # Hiển thị ảnh gốc
    cv2.imshow('Decoded Image', img_decoded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đọc ảnh đã được giấu thông tin
encoded_img = cv2.imread('image//an_ma.png', 0)

# Đọc ảnh gốc (lon.jpg)
cover_img = cv2.imread('image//lon.jpg', 0)

# Đọc ảnh giấu (ma_qrcode.png)
secret_img = cv2.imread('image//ma_qrcode.png', 0)

# Giải mã và lưu ảnh gốc
giai_ma_va_luu(cover_img, np.zeros_like(secret_img), 'image//giai_ma_lon.jpg')

# Giải mã và lưu ảnh giấu
giai_ma_va_luu(encoded_img, secret_img, 'image//giai_ma_ma_qrcode.png')
