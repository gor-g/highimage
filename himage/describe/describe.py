import numpy as np



def nonAngularContourSignature(contour, c, interpSize = 500):
    """ finds a contour signature by iterating on the points of the contour. The contour can be obtained with cv2.findContours()
    unlike the conventional signature that is obtained by rotating around the central point with a constant angular step this function folows the points of the contour.
    
    Parameters
    ----------
    contour : the contour to analyse
    c : the central point of the polar coordinates
    interpSize : in order to be comparable the signatures must be vectors of a fixed size, so before computing the fft we interpolate the curve of the distance of the contour from the point c to a vector of size interpSize and only than we compute the fft
    
    """
    
    contour = np.array([p[0] for p in contour])

    norms =np.linalg.norm(contour - c,  ord=2, axis=1)
    norms = np.interp(np.linspace(0, interpSize, interpSize), np.linspace(0, interpSize, norms.size ),norms  )
    res = np.abs(np.fft.fft(norms))
    res /= res.max()

    res = res+np.roll(res, 1)+np.roll(res, 2)+np.roll(res, -1)+np.roll(res, -2)

    return res/res.max()
