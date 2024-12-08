import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column, bins=30):
    """
    Plots a histogram for a specified column.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_scatter(df, x_col, y_col, hue_col=None):
    """
    Plots a scatter plot with optional color encoding.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, palette='viridis')
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


