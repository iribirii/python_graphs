def aim_vs_nbo(filename, color, ax, col_x, col_y, d_label):
    
    ''' 
    Function to create AIM rhos vs NBO E(2) graphs including 2nd order polynomial correlation.
    
    :param filename: name of the CSV file (\\t separated in this case).
    :type filename: string
    
    :param color: color for plotting the data. Can be hex code or python color.
    :type color: string
    
    :param ax: axis in which you want to plot the data
    :type ax: matplotlib axis

    :param col_x: column name for x values
    :type col_x: string
    
    :param col_y: column name for y values
    :type col_y: string

    :param d_label: label for the current data plotted
    :type d_label: string
    '''
    
    import pandas as pd
    from scipy.optimize import curve_fit
    from sklearn.metrics import r2_score
    import numpy as np
    import matplotlib

    # Read data
    d = pd.read_csv(filename, delimiter=',')

    # Data to numpy for plotting
    x = d[col_x].to_numpy()
    y = d[col_y].to_numpy()

    # Regression y = a*x**2 + b*x
    popt, pcov = curve_fit(fit_func, x, y)

    # Generate the x and y values for plotting the fitted curves
    x_fit = np.linspace(x.min(), x.max(), 100)
    y_fit = fit_func(x_fit, *popt)

    # Calculates the r2 score using the original Y values and the generated Y values of the fitted curve
    y_r2 = fit_func(x, *popt)
    r2 = r2_score(y, y_r2)
    
    # Change the fonsize 
    font = {'size'   : 12}
    matplotlib.rc('font', **font)

    # Change the labels of the axis
    ax.set_xlabel(f'{col_x}')
    ax.set_ylabel(f'{col_y}')

    # Plot the original values with scattering
    ax.scatter(x, 
               y, 
               label=d_label,
               color=color)

    # Plot the fitted curve 
    ax.plot(x_fit,
            y_fit,
            color=color,
            lw=1,
            label=f'$y = {popt[0]:.2f}x^2 + {popt[1]:.2f}x, r^2={r2:.4f}$')

def fit_func(x, a, b):
    '''
    Second order function to use for fitting the data and then generate the Y values to plot the curve.
    It forces the curve to go through the origin (0,0).

    :param x: X values for generating the corresponding Y 
    :type x: List[float]

    :param a: First parameter of the function
    :type a: float

    :param b: Second parameter of the function
    :type b: float
    '''
    
    return a * x**2 + b * x

def main():
    '''
    Example of a second order polynomial fitted plot.
    Fits the curve, calculates R2 and shows the equation.
    '''

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1,1,figsize=(12,6))

    ax.set_title('Example graph with 2nd order polynomial correlation')
    aim_vs_nbo('./example_1.csv', '#8f96bf', ax, 'Xvalues', 'Yvalues', 'data1')
    aim_vs_nbo('./example_2.csv', '#716cb0', ax, 'Xvalues', 'Yvalues', 'data2')
    aim_vs_nbo('./example_3.csv', '#333c70', ax, 'Xvalues', 'Yvalues', 'data3')

    ax.legend(
        frameon=False,      # No box for the legend
        markerfirst=False,  # Put the markers after the text (left aligned)
        loc='lower right'   # Locate legend at the bottom right
    )

    plt.savefig(
        'example_2nd_order_polynomial_fit.png',
        dpi=300,
        transparent=True,
        format='png'
    )


if __name__ == '__main__':
    main()
