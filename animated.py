from PIL import Image, ImageSequence
import qrcode

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data("https://github.com/Fahad-Al-Maashani")
qr.make()
img = qr.make_image(fill_color="black", back_color="white")

frames = []
for i in range(10):
    frame = img.copy().convert("RGBA").rotate(i * 36)
    frames.append(frame)

frames[0].save("animated_qr.gif", save_all=True, append_images=frames, duration=100, loop=0)
print("✅ Animated QR Code saved as animated_qr.gif")
