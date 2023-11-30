import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = None,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size = 10,
    border = 4,
)

data = "Watermarking_Using_QR_Code"
qr.add_data(data)
qr.make(fit= True)

img = qr.make_image(fill_color ="black", back_color ="white")
img.save("image\\QR_Image.jpg")
image = Image.open("image\\QR_Image.jpg")

new_image = image.resize((400,400))
new_image.save("image\\QR_Image.jpg")
