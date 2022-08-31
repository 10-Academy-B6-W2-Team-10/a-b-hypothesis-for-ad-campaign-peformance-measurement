import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path: str):
    df = pd.read_csv(path)
    return df

def data_shape(df):
    print(f" There are {df.shape[0]} rows and {df.shape[1]} columns")

"""how many missing values exist or better still what is the % of missing values in the dataset?"""

def data_types(df):
    t = df.dtypes.value_counts()
    return t

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

def top_values(df:pd.DataFrame, column:str, top:int) -> None:
    values = df[column].value_counts()
    topdf = df.loc[df[column].isin(list(values[:top].index))]
    return topdf

def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(20,10))
    fig = sns.countplot(data = df, x = column, order = df[column].value_counts().index)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(column, fontsize=20)
    plt.ylabel('Absolute frequencies', fontsize=20)
    for i in range(len(df[column].value_counts())):
        fig.text(i, (df[column].value_counts()[i])/2, str(df[column].value_counts()[i]), fontdict = dict(color = 'black', fontsize = 30), horizontalalignment = 'center')

def multi_plot_count(df:pd.DataFrame, column:str, hue: str) -> None:
    plt.figure(figsize=(20,10))
    fig = sns.countplot(data = df, x = column, hue=hue)
    plt.title(f'Distribution of {column} per {hue}', size=20, fontweight='bold')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(column, fontsize=20)
    plt.ylabel('Absolute frequencies', fontsize=20)

    for p in fig.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        fig.annotate(f'{(height)}', (x + width/2, y + height*1.02), ha='center', size = 15)

