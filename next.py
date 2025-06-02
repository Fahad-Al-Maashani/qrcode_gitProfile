import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create a QR code with error correction
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=5,
)

qr.add_data("https://github.com/Fahad-Al-Maashani")
qr.make(fit=True)

# Generate an image with custom colors
img = qr.make_image(fill_color="blue", back_color="white")
img.save("custom_qr.png")
