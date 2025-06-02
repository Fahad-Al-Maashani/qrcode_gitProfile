from PIL import Image
import qrcode

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://github.com/Fahad-Al-Maashani")
qr.make(fit=True)

# Generate QR Code Image
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Open logo image
logo = Image.open("logo.png")  # Ensure the file exists

# Resize and position the logo
logo_size = 60
logo = logo.resize((logo_size, logo_size))
img.paste(logo, (img.size[0] // 2 - logo_size // 2, img.size[1] // 2 - logo_size // 2), mask=logo)

# Save the final QR code
img.save("qr_with_logo.png")
