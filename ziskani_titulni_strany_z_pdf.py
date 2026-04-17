from PIL import Image

from pdf2image import convert_from_path

images = convert_from_path("/home/lukas/Python/Porgazeen/casopisy/91.pdf", first_page=1, last_page=1)
images[0].save("/home/lukas/Python/Porgazeen/titulni_strany/91.jpg", "JPEG")

img = Image.open("/home/lukas/Python/Porgazeen/titulni_strany/91.jpg")

resized = img.resize((198, 280), Image.LANCZOS)

resized.save("/home/lukas/Python/Porgazeen/titulni_strany/91.jpg")