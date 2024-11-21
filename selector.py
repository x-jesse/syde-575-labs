import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import RectangleSelector
from skimage.io import imread
class Selector:
    def __init__(self, ax):
        self.RS = RectangleSelector(ax, self.line_select_callback,
                                     useblit=True,
                                       button=[1, 3],  
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
        self.bbox = [None, None, None, None]
        
    def line_select_callback(self,eclick, erelease):
        'eclick and erelease are the press and release events'
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        self.bbox = [int(y1), int(y2), int(x1), int(x2)]
    def get_bbox(self):
        return self.bbox

# Display the image as usual
img = imread('degraded.tif').astype(np.float64) / 255
ax = plt.gca()
ax.imshow(img, vmax=1, vmin=0, cmap='gray')
# Create Selector class with the current plot axis
select = Selector(ax)
# Show the result
plt.show()

print(select.bbox)