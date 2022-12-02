import matplotlib.pyplot as plt


def multimshow(images, titles=None, cmaps=None, vmin = None, vmax = None, n_cols=2, axisOn = False, figsize=None, colwidth=None ):
    """
    shows mutiple images in one plot
    :param images: list or tuple of images
    :param titles: list or tuple of titles
    :param cmaps: list or tuple of cmaps or integers (0 for None and 1 for 'gray') or a singla cmap or an integer
    :param n_cols: int, number of columns of the resulting plot
    :param axisOn: turn on and of the axis of the plots
    :param figsize: tuple, of floats, representing the dimensions of the plot
                    int or float represntig the desired width of the output, the heigth will be calculated automatically
    :param colwidth: int or float representig the width of the column, can be given instead of a figsize. n_cols = 3 and colwidth = 5 will give the same output as colwidth = 3 and figsize = 15
    :return: None
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
