import cv2
import numpy as np
import pywt

# Load the cover image in grayscale
cover_img = cv2.imread('thuyvan\\an_ma.jpg')

# Check if the image is loaded successfully
if cover_img is None:
    print("Error: Could not load the image.")
    exit()

# Apply wavelet transform
coeffs = pywt.dwt2(cover_img, 'haar')
cA, (cH, cV, cD) = coeffs

# Define the 'mang' function (assuming it's designed to manipulate the coefficients)
def mang(cover):
    U, s, V = np.linalg.svd(cover)
    secret_cA = np.zeros_like(cover)
    alpha = 0.9
    for i in range(len(cover)):
        mau = U[i,:10] * s[:10] @ V[:10, :]
        for j in range(len(cover[0])):
            if (i < len(secret_cA) and j < len(secret_cA[0])):
                secret_cA[i][j] = (cover[i][j] - mau[j] * alpha) * (1 - alpha)
    return secret_cA

# Load the secret image in grayscale
secret_img = cv2.imread('thuyvan\\ma_qrcode.png', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if secret_img is None:
    print("Error: Could not load the secret image.")
    exit()

# Apply wavelet transform to the secret image
secret_coeffs = pywt.dwt2(secret_img, "haar")
cA, (secret_cH, secret_cV, secret_cD) = secret_coeffs

# Create a new array with the same shape as cA and apply the 'mang' function
new_shape = cA.shape
new_array = np.zeros(new_shape)
new_array[:new_array.shape[0], :new_array.shape[1]] = mang(cA)[:new_array.shape[0], :new_array.shape[1]]

# Update the secret coefficients with the modified cA
secret_coeffs = new_array, (secret_cH, secret_cV, secret_cD)

# Inverse wavelet transform to obtain the new secret image
secret_img_new = pywt.idwt2(secret_coeffs, 'haar')

# Save the result
cv2.imwrite('thuyvan\\secret_img.jpg', secret_img_new)
