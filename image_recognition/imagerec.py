from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/numbers/y0.5.png')
image_array = np.asarray(i)
plt.imshow(image_array)
print image_array
plt.show()
