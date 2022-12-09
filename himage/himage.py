# Copyright (C) 2022, Gog G.
#
# License: MIT 


import matplotlib.pyplot as plt
import cv2
cv = cv2


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
        assert  (figsize == None), "if colwidth is not None than is being deduced automatically"
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






#def multPlot(args, titles=None, n_cols=2, axisOn = True, figsize=None, colwidth=None ):
    #"""shows mutiple images in one plot
    #Parameters
    #----------
    #args : list or tuple of images
    #titles : list or tuple of titles
    #cmaps : list or tuple of cmaps or integers (0 for None and 1 for 'gray') or a singla cmap or an integer
    #n_cols : int, number of columns of the resulting plot
    #axisOn : turn on and of the axis of the plots
    #figsize : tuple, of floats, representing the dimensions of the plot
              #int or float represntig the desired width of the output, the heigth will be calculated automatically
    #colwidth : int or float representig the width of the column, can be given instead of a figsize. n_cols = 3 and colwidth = 5 will give the same output as colwidth = 3 and figsize = 15
    #Returns
    #-------
    #None
    #"""


    #n_ims = len(args)
    #n_rows = int(np.ceil(n_ims/n_cols))
    #if colwidth != None:
        #assert  (figsize == None), "if colwidth is not None than is being deduced automatically"
        #figsize = colwidth * n_cols


    #if type(figsize)!=tuple and figsize!=None:
        #figsize = (figsize, figsize/n_cols * n_rows)





    #fig = plt.figure(figsize=figsize)

    #for i, argTuple in enumerate(args):
        #print("\n args = ",argTuple)
        #print("\n *args = ",*argTuple)
        #fig.add_subplot(n_rows, n_cols, i+1)
        #plt.ylim(0, 1)
        #if not axisOn:
            #plt.axis('off')
        #if titles:
            #plt.title(titles[i])
        #plt.plot(*argTuple)
    #plt.show()

    #return None

#a1=np.arange(0,10, 1)
#a2 = np.arange(0,1, 1/10)



print(a1)
print(a2)
multPlot(((np.hstack((a1, a1)), np.hstack((a2, a2/2))), (a1, a2/2)))







def rescle(im, scale, returnTransforMatrix = False):
    """rescale image
    Parameters
    ----------
    im : ndarray
    scale : float
    returnTransforMatrix : bool, optional,  if true, returns the transformation matrix that was applied on the image

    Returns
    -------
    im :  ndarray, rescaled image
    (im, tfoMat) : tuple, the rescaled image and the transformation matrix used to rescale the image
    """
    rows, cols = im.shape
    tfoMat = cv.getRotationMatrix2D((cols/2, rows/2), 0, scale)
    
    if returnTransforMatrix:
        return cv.warpAffine(im, tfoMat, (cols, rows)), tfoMat
    
    else:
        return cv.warpAffine(im, tfoMat, (cols, rows)) 

def rotate(im, rot, returnTransforMatrix = False):
    """rotates an image around it's central point'
    Parameters
    ----------
    im : ndarray
    rot : float, the rotation angle in degrees
    returnTransforMatrix : bool, optional if true, returns the transformation matrix that was applied on the image
    
    Returns
    -------
    im :  rotated image
    (im, tfoMat) : tuple, the rotated image and the transformation matrix used to rescale the image
    """
    rows, cols = im.shape
    tfoMat = cv.getRotationMatrix2D((cols/2, rows/2), rot, 1)
    
    if returnTransforMatrix:
        return cv.warpAffine(im, tfoMat, (cols, rows)), tfoMat

    else:
        return cv.warpAffine(im, tfoMat, (cols, rows))







def standardize(im, side = 64):
    """ Standardize one channel images by adding symetrical "stretch" padding on the sides along the shortest axis 
    If width < height, the border columns are copyed on both sides till the width is equal to height
    
    """
    r, c = im.shape
    new_h = np.zeros((max(r, c), max(r, c)), dtype='uint8')
    if r > c:
        new_h[:,:(r - c) // 2] = np.repeat(im[:, 1].reshape(-1, 1), (r - c) // 2, axis=1)
        new_h[:, (r - c) // 2 + c :] = np.repeat(im[:, -2].reshape(-1, 1),
                                                 (r -( (r - c) // 2 + c) ),
                                                 axis=1)
        new_h[:,(r - c) // 2:(r - c) // 2 + c] = im
        return  np.uint8(cv2.resize(new_h, (side, side)))
    else:
        raise NotImplementedError("this function isn't implemented for images wider than their height, use standardize(im.T).T if necessery")


def standardizeC3(im, side=64):
    """ Standardize 3 channel images by adding symetrical "stretch" padding on the sides along the shortest axis 
    If width < height, the border columns are copyed on both sides till the width is equal to height

    """
    return cv2.merge([standardize(c, side) for c in cv2.split(im)])
