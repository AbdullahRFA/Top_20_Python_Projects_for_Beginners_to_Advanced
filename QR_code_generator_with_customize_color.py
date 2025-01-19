from platform import version
import qrcode
from PIL import Image

# Create a QRCode instance with appropriate parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4  # Corrected parameter name
)

# Add data to the QR code
qr.add_data(input("Enter your link or text to generate QR code: "))
qr.make(fit=True)

# Create the QR code image with customized colors
img = qr.make_image(fill_color="red", back_color="white")

# Save the generated QR code image
img.save(input("Enter the file name for the QR code (e.g., qrcode.png): "))