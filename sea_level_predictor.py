from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    def myfunc(x):
        return slope * x + intercept

    x_list = df['Year'].tolist()
    x_list.extend(list(range(2014,2051)))
    mymodel = list(map(myfunc, x_list))
    plt.plot(x_list, mymodel, color='red')

    # Create second line of best fit
    x_list = df['Year'].tolist()
    y_list = df['CSIRO Adjusted Sea Level'].tolist()
    index = x_list.index(2000)
    slope, intercept, r, p, std_err = linregress(x_list[index::], y_list[index::])
    x_list.extend(list(range(2014,2051)))
    mymodel = list(map(myfunc, x_list[index::]))
    plt.plot(x_list[index::], mymodel, color='black')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()