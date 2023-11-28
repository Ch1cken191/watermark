import cv2
import numpy as np

# Đọc ảnh vào
image = cv2.imread('image//secret_img.png')

# Chuyển đổi ảnh sang không gian màu RGB (OpenCV sử dụng BGR mặc định)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Tạo mặt nạ dựa trên điều kiện màu
mask = np.all(image_rgb >= [86, 86, 86], axis=-1)

# Thiết lập màu trắng cho các pixel thỏa mãn điều kiện, và màu đen cho các pixel còn lại
image_rgb[mask] = [255, 255, 255]
image_rgb[~mask] = [0, 0, 0]

# Chuyển đổi ảnh RGB trở lại BGR
result_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# Hiển thị ảnh gốc và ảnh kết quả
cv2.imwrite("image//re_secret_image.png",result_image)
cv2.imshow('Original Image', image)
cv2.imshow('Result Image', result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
