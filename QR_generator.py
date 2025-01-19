import qrcode as qr


qr_code = qr.make(input("Enter your link or text to generate QR code : "))

qr_code.save(input("Enter the name of QR code : ")) 