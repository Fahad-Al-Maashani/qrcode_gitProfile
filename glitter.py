import cv2
import numpy as np

qr_image = cv2.imread("basic_qr.png")

for _ in range(100):
    x, y = np.random.randint(0, qr_image.shape[1]), np.random.randint(0, qr_image.shape[0])
    qr_image[y:y+2, x:x+2] = [255, 255, 255]

cv2.imwrite("glitter_qr.png", qr_image)
print("✨ Glitter QR Code saved as glitter_qr.png")
