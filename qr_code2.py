import qrcode
from PIL import Image
import qrcode.constants
code=input("Enter the link of the page you want to convert into QR code: ")
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data(code)
qr.make(fit=True)
code_color=input("Enter the color of the QR Code:")
background=input("Enter the background color of the QR Code:")
img=qr.make_image(fill_color=code_color,back_color=background)
img.save('QR.png')