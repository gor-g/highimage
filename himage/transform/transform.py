import cv2
import numpy as np


def rescale(im, scale, returnTransforMatrix = False):
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
    tfoMat = cv2.getRotationMatrix2D((cols/2, rows/2), 0, scale)
    
    if returnTransforMatrix:
        return cv2.warpAffine(im, tfoMat, (cols, rows)), tfoMat
    
    else:
        return cv2.warpAffine(im, tfoMat, (cols, rows)) 


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
    tfoMat = cv2.getRotationMatrix2D((cols/2, rows/2), rot, 1)
    
    if returnTransforMatrix:
        return cv2.warpAffine(im, tfoMat, (cols, rows)), tfoMat

    else:
        return cv2.warpAffine(im, tfoMat, (cols, rows))







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

