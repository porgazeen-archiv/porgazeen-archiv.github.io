from random import randint as ri

from PIL import Image

img = Image.open("/home/lukas/Python/Porgazeen/titulni_strany/90.jpg")

resized = img.resize((198, 280), Image.LANCZOS)

resized.save("/home/lukas/Python/Porgazeen/titulni_strany/90.jpg")