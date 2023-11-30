import numpy as np
from PIL import Image
import cv2
import qrcode

def logistic_map(r, x0, n):
    xn = x0
    results = []
    for i in range(n):
        xn = r * xn * (1 - xn)
        results.append(xn)
    return results

def decrypt_image(encrypted_image_path, r, x0):
    image = Image.open(encrypted_image_path).convert('L')
    image_array = np.array(image)
    a, b = image.size[0], image.size[1]
    n = a * b
    key = np.array(logistic_map(r, x0, n))
    ma = key[:image_array.size].reshape(image_array.shape)
    ma = (ma * n).astype(np.uint8)
    image_array = (image_array * 255).astype(np.uint8)
    decrypt_image = image_array ^ ma
    decrypt_image = Image.fromarray(decrypt_image)

    return decrypt_image

def read_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    value, pts, qr_code = detector.detectAndDecode(img)
    return value

encrypted_image_path = 'image\\en_QR_Image.png'
decrypt_image_path = 'image\\de_QR_Image.jpg'

r = 4
x0 = 0.5
decrypt_image = decrypt_image(encrypted_image_path, r, x0)
decrypt_image.save(decrypt_image_path)

# Đọc thông điệp từ QR code đã giải mã
decrypted_message = read_qr_code(decrypt_image_path)
print("Decrypted Message:", decrypted_message)
