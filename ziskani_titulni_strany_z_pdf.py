from PIL import Image

from pdf2image import convert_from_path

cislo = "93"

images = convert_from_path(f"/home/lukas/Python/Porgazeen/casopisy/{cislo}.pdf", first_page=1, last_page=1)
images[0].save(f"/home/lukas/Python/Porgazeen/titulni_strany/{cislo}.jpg", "JPEG")

img = Image.open(f"/home/lukas/Python/Porgazeen/titulni_strany/{cislo}.jpg")

resized = img.resize((198, 280), Image.LANCZOS)

resized.save(f"/home/lukas/Python/Porgazeen/titulni_strany/{cislo}.jpg")