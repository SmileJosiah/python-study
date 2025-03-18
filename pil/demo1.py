import PIL
from PIL import Image

image = Image.open(r'C:\Users\XingyiZhu\Pictures\test\f02106f3ae27f97f53f38e14c3808303.png')
image.show()
image_1 = image.convert('1')
image_1.show()
image_l = image.convert('L')
image_p = image.convert('P')
image_l.show()
image_p.show()