from PIL import Image
import numpy as np

i = Image.open('images/dot.png')
image_array = np.asarray(i)

print image_array
