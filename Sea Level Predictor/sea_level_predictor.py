import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    to_2050 = range(df['Year'].min(), 2051)

    ax.plot(to_2050, (line1.intercept + line1.slope * to_2050))

    # Create second line of best fit
    from_2000 = df.loc[df['Year'] >= 2000]

    line2 = linregress(from_2000['Year'], from_2000['CSIRO Adjusted Sea Level'])

    to_2050 = range(from_2000['Year'].min(), 2051)

    ax.plot(to_2050, (line2.intercept + line2.slope * to_2050))

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
