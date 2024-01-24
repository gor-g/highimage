
import matplotlib.pyplot as plt
import numpy as np
from warnings import warn


def imshow(im, title=None, cmap=None, limits = None, dpi = None, axisOn = False, figsize=None):
    """shows an image with matplotlib
    Parameters
    ----------
    im : ndarray
    title : string, optional
    cmap : string, values are the same as in matplotlib.pyplot.imshow. 
            If None value is provided and the image has a single channel, the
            cmap is set 'gray' instead of matplotlib's default cmap for gray images.
    limits : (vmin, vmax) a pair of int or float values representig the minimal pixel intensity of the plot.
    dpi : int, dots per inch
    axisOn : turn on and of the axis of the plots
    figsize : tuple, of floats, representing the dimensions of the plot
              int or float represntig the desired width of the output, the heigth will be calculated automatically
    """


    if limits is None:
        vmin = 0
        if isinstance(im.flat[0], np.floating) and im.max() <= 1:
            vmax = 1
        else:
            vmax = 255
    else:
            vmin, vmax = limits


    if cmap is None and im.ndim == 2:
        cmap = 'gray'

    if type(figsize)!=tuple and figsize!=None:
        w, h = im.shape
        figsize = (h/w * figsize, figsize)

    plt.figure(figsize=figsize, dpi=dpi, frameon=False)

    if not axisOn:
        plt.axis('off')

    plt.tight_layout()
    plt.imshow(im, cmap=cmap, vmin = vmin, vmax=vmax)
    if title:
        plt.title(title)
    plt.show()
    
    return None




def multimshow(images, titles=None, cmaps=None, vmin = None, vmax = None, n_cols=2, axisOn = False, figsize=None, colwidth=None ):
    """shows mutiple images in one plot
    Parameters
    ----------
    images : list or tuple of images
    titles : list or tuple of titles
    cmaps : list or tuple of cmaps or integers (0 for None and 1 for 'gray') or a singla cmap or an integer
    vmin : int or float representig the minimal pixel intensity of the plot
    vmax : int or float representig the maximal pixel intensity of the plot
    n_cols : int, number of columns of the resulting plot
    axisOn : turn on and of the axis of the plots
    figsize : tuple, of floats, representing the dimensions of the plot
              int or float represntig the desired width of the output, the heigth will be calculated automatically
    colwidth : int or float representig the width of the column, can be given instead of a figsize. n_cols = 3 and colwidth = 5 will give the same output as colwidth = 3 and figsize = 15
    Returns
    -------
    None
    """


    n_ims = len(images)
    n_rows = int(np.ceil(n_ims/n_cols))
    if colwidth != None:
        if figsize != None:
            warn("If colwidth is not None, figsize is being deduced automatically. The user provided figsize is ignored.")
        figsize = colwidth * n_cols


    if type(figsize)!=tuple and figsize!=None:
        figsize = (figsize, figsize/n_cols * n_rows)



    # translating the cmaps in to a format understandable by matplotlib
    if not (type(cmaps)== list or type(cmaps)==tuple):
        if cmaps in [0,1]:
            cmaps = [None, 'gray'][cmaps]
        cmaps = [cmaps for i in range(n_ims)]
    else:
        cmaps=list(cmaps)
        for i,c in enumerate(cmaps):
            if c == 1:
                cmaps[i]="gray"
            elif c == 0:
                cmaps[i]=None


    if not (type(vmin) == list or type(vmin)==tuple):
        vmin = [vmin for i in range(n_ims)]
    if not (type(vmax) == list or type(vmax)==tuple):
        vmax = [vmax for i in range(n_ims)]


    fig = plt.figure(figsize=figsize)

    for i, im in enumerate(images):
        fig.add_subplot(n_rows, n_cols, i+1)
        if not axisOn:
            plt.axis('off')
        if titles:
            plt.title(titles[i])
        plt.imshow(im, cmap=cmaps[i], vmin = vmin[i], vmax=vmax[i])
    plt.show()
    
    return None