import cv2
import numpy as np
import matplotlib.pyplot as plt

def compare_images(image1, image2):
    # Đọc hai hình ảnh
    img1 = cv2.imread(image1, 0)
    img2 = cv2.imread(image2, 0)

    # Tính toán histogram cho hai hình ảnh
    hist_img1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist_img2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

    # Chuẩn hóa histogram
    hist_img1 /= hist_img1.sum()
    hist_img2 /= hist_img2.sum()

    # Tính độ tương đồng giữa hai histogram
    similarity = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)

    return similarity

# File ảnh cần so sánh
image1_path = "image//en_QR_Image.png"
image2_path = "image//extracted_QR.png"

# So sánh hai ảnh
similarity_score = compare_images(image1_path, image2_path)

# Hiển thị kết quả
print(f"Similarity Score: {similarity_score}")

# Trực quan hóa hai hình ảnh và kết quả đánh giá tương đồng
img1 = cv2.imread(image1_path)
img2 = cv2.imread(image2_path)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axes[0].set_title('Image 1')

axes[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axes[1].set_title('Image 2')

axes[2].text(0.5, 0.5, f"Similarity Score: {similarity_score:.4f}", 
             ha='center', va='center', fontsize=12, color='blue')
axes[2].axis('off')
axes[2].set_title('Similarity Score')

plt.show()
