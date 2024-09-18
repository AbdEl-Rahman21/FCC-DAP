import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype('int64')
df['cholesterol'] = (df['cholesterol'] != 1).astype('int64')
df['gluc'] = (df['gluc'] != 1).astype('int64')

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = pd.DataFrame(df_cat.value_counts()).reset_index()

    df_cat.columns = ['cardio', 'variable', 'value', 'total']

    fig = sns.catplot(kind='bar', data=df_cat, x='variable', y='total', col='cardio', hue='value',
                      order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']).figure

    fig.savefig('catplot.png')

    return fig

def draw_heat_map():
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
                     (df['height'] >= df['height'].quantile(0.025)) &
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) &
                     (df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()

    mask = np.triu(np.ones(corr.shape)).astype(bool)

    fig, ax = plt.subplots(figsize=(11, 9))

    ax = sns.heatmap(data=corr, mask=mask, annot=True, linewidth=0.5, fmt='.1f', vmax=0.3)

    fig.savefig('heatmap.png')
    
    return fig
