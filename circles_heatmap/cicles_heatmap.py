def circles_heatmap(ax, x, y, s, n_x, n_subx):
    '''
    Function to create a heatmap in which the size of the cicles corresponds to the value of a magnitud.
    It is colored by columns for each block.

    :param ax: axis in which the graph will be plotted.
    :type ax: matplotlib axis 

    :param x: array with the names of the columns to plot.
    :type x: string array

    :param y: array with the names of the rows to plot.
    :type y: string array

    :param s: array with the values for the size of the circles.
    :type s: float array

    :param n_x: number of groups that will be plotted
    :type n_x: int

    :param n_subx: number of sub-groups that form the groups.
    :type n_subx: int

    '''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.pyplot import rcdefaults, rc

    # Image size and settings 
    dpi=plt.rcParams['figure.dpi'] # take dpi from settings 
