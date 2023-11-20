import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = None,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size = 10,
    border = 4,
    )
data = "Hello Thanh"
qr.add_data(data)
qr.make(fit =True)

img = qr.make_image(fill_color = "black",bacl_color = "white")
img.save("thuyvan\\qrcode.jpg")
image = Image.open("thuyvan\\qrcode.jpg")
new_image = image.resize((400,400))
new_image.save("thuyvan\\new_qrcode.jpg")