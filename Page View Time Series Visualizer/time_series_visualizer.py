import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    plt.rc('font', size=20)

    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)

    ax.plot(df, color='red', linewidth=3)

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    Months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    df_bar = df.rename_axis('date').reset_index()

    df_bar['year'] = df_bar['date'].dt.strftime('%Y')
    df_bar['month'] = df_bar['date'].dt.strftime('%B')

    df_bar.drop('date', axis=1, inplace=True)

    df_bar = df_bar.groupby(['year', 'month']).mean()

    # Draw bar plot
    plt.rc('font', size=20)

    fig, ax = plt.subplots(figsize=(15.14, 13.3))

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    ax.ticklabel_format(style='plain')
    ax.tick_params(axis='x', labelrotation=90)

    sns.barplot(df_bar, x='year', y='value', hue='month',
                width=0.5, legend='full', hue_order=Months, palette='bright')

    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    df_box = df.rename_axis('date').reset_index()

    df_box['year'] = df_box['date'].dt.strftime('%Y')
    df_box['month'] = df_box['date'].dt.strftime('%b')

    df_box.drop('date', axis=1, inplace=True)
    
    # Draw box plots (using Seaborn)
    plt.rc('font', size=20)

    fig, ax = plt.subplots(figsize=(28.8, 10.8), ncols=2)

    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(df_box, x='year', y='value', ax=ax[0],
                palette='bright', legend=False, hue='year')
    
    ax[0].yaxis.set_ticks(range(0, 220000, 20000))

    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    sns.boxplot(df_box, x='month', y='value', ax=ax[1],
                palette='bright', legend=False, hue='month', order=Months)
    
    ax[1].yaxis.set_ticks(range(0, 220000, 20000))

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
