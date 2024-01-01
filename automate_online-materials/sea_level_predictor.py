import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    #Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    # Use linregress to get the slope and y-intercept of the line of the best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'],data['CSIRO Adjusted Sea Level'])
    # Create a list of x-values for the line of best fit
    x = list(range(1880,2051))
    # Use the slope and y-intercept to calculate y-values for the line of best fit
    y = [slope * xi + intercept for xi in x]
    # Add the line of best fit to the scatter plot
    plt.plot(x,y,color='red', label='Line of best fit (1880-2016)')

    # Set the limits for the x and y axis
    plt.xlim ( 1880, 2100 )
    plt.ylim ( -2, 16 )

    # Use the slope and y-intercept to predict the sea level rise in 2050
    year2050 = 2050
    predicted_sea_level = slope * year2050 + intercept
    print ( "Predicted sea level rise in 2050: {:.2f} inches".format ( predicted_sea_level ) )

    # Create second line of best fit
    # Get the data from year 2000 to the most recent year
    recent_data=data[data['Year']>=2000]
    # Get the slope and y-intercept of the line of best fit for the recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'],recent_data['CSIRO Adjusted Sea Level'])
    # Create a line of best fit for the recent data and plot it
    years_recent = range(2000,2051)
    sea_level_recent = slope_recent*years_recent+intercept_recent
    plt.plot(years_recent,sea_level_recent,'green',label='Line of best fit (2000-2016)')


    # Add labels and title
    plt.xlabel ( 'Year' )
    plt.ylabel ( 'Sea Level (inches)' )
    plt.title ( 'Rise in Sea Level' )
    # Add a legend to the plot
    plt.legend()

    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig ( 'sea_level_plot.png' )
    return plt.gca ()

draw_plot()

