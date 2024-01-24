import cv2 
import numpy as np
from himage import imshow, multimshow

im_gray = np.ones((20, 10))*.9


imshow(im_gray)

multimshow( [im_gray * 0.05 * i for i in range(20)], 
            titles=[str(i) for i in range(20)],
            cmap='gray',
            n_cols=5,
            figsize=10,
            colwidth=2
)


im_yellow = np.ones((20, 10, 3))*.9
im_yellow[:,:,2] = 0

imshow(im_yellow)
imshow(im_yellow, cmap='gray') # expecting the cmap to be ignored