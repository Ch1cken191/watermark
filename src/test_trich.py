import cv2
import numpy as np
import pywt
import qrcode

def embed_qr_code_into_image(original_img_path, qr_code_img_path, stego_img_path):
    # Đọc ảnh lớn
    large_img = cv2.imread(original_img_path)

    # Đọc ảnh QR code
    qr_code_img = cv2.imread(qr_code_img_path, cv2.IMREAD_GRAYSCALE)

    # Chuyển đổi ảnh QR code thành mảng số (0 và 255)
    _, qr_code_img_binary = cv2.threshold(qr_code_img, 128, 255, cv2.THRESH_BINARY)

    # Nhúng thông tin từ ảnh QR code vào ảnh lớn
    stego_img = large_img.copy()
    stego_img[:qr_code_img.shape[0], :qr_code_img.shape[1], 0] += qr_code_img_binary

    # Lưu ảnh đã nhúng
    cv2.imwrite(stego_img_path, stego_img)

def extract_qr_code_from_image(stego_img_path, qr_code_shape):
    # Đọc ảnh đã nhúng
    stego_img = cv2.imread(stego_img_path)

    # Trích xuất thông tin từ ảnh đã nhúng
    extracted_qr_code = stego_img[:qr_code_shape[0], :qr_code_shape[1], 0]

    return extracted_qr_code

def reverse_dwt(stego_img, levels=1):
    # Thực hiện DWT
    coeffs = pywt.dwt2(stego_img, 'bior1.3', level=levels)

    # Thực hiện IDWT để có ảnh gốc
    original_img = pywt.idwt2(coeffs, 'bior1.3')

    return original_img

# Tạo ảnh QR code từ một đoạn văn bản (ví dụ: URL)
url_text = "https://www.example.com"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url_text)
qr.make(fit=True)

qr_code_img = qr.make_image(fill_color="black", back_color="white")
qr_code_img.save('image//qr_code.png')

# Nhúng ảnh QR code vào ảnh lớn
embed_qr_code_into_image('image//lon.jpg', 'image//qr_code.png', 'image//stego_image_with_qr.png')

# Kích thước của ảnh QR code gốc
qr_code_shape = (qr_code_img.size[1], qr_code_img.size[0], 3)

# Trích xuất thông tin từ ảnh đã nhúng (ví dụ: QR code)
extracted_qr_code = extract_qr_code_from_image('image//stego_image_with_qr.png', qr_code_shape)

# Thực hiện quy trình ngược DWT để khôi phục ảnh gốc
recovered_original_img = reverse_dwt(extracted_qr_code)

# Lưu ảnh gốc đã khôi phục
cv2.imwrite('image//recovered_original_img.jpg', recovered_original_img)
