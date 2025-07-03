import qrcode as qr
img= qr.make("https://www.geeksforgeeks.org/")
img.save("gfg.png")
img2=qr.make("https://www.facebook.com/soma.chakraborty.275013")
img2.save("Soma.png")