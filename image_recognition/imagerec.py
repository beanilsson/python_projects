from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/dot.png')
image_array = np.asarray(i)
plt.imshow(image_array)
plt.show()
