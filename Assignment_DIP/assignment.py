from PIL import Image
import numpy as np
cover = Image.open("cover.png")
secret = Image.open("secret.png")
secret = secret.resize(cover.size)

cover = np.array(cover)
secret = np.array(secret)

stego = (cover & 0xF0) | (secret >> 4)

stego_img = Image.fromarray(stego.astype('uint8'))
stego_img.save("stego.png")

print("Image hidden successfully!")
