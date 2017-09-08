import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/dotndot.png')
image_array = np.asarray(i)
plt.imshow(image_array)
plt.show()
