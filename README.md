A set of various convenient functions useful in image processing, written in Python.

# Why This Exists?

As someone working in image processing, the only time I've used Pillow was when I was working on a project that had already been using Pillow. I've always ended up having to perform advanced matrix operations or train AI, in both cases, I had to work with `np.arrays`.

This library is designed to easily give you access to images as `np.arrays`:

- The images are already normalized by default to have `float` values between 0 and 1.
- The images come already in RGB, instead of OpenCV's default BGR.
- The functions used to plot the images are using `matplotlib`, which is compatible with `.ipynb` notebooks.
- It's easy to plot multiple images in a clean layout using `multimshow`.


## Example of usage

```py
from himage import imshow, multimshow, imread

im = imread("image.png")

imshow(im)
multimshow([im, im, im], titles = ['title 1', 'title 2', 'title 3'], n_cols=3)
```
