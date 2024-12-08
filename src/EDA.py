import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def data_describe(df):
    # Summary statistics for numerical data
    return df.describe()

def info_data(df):
    # Basic information of the column of the data
    return df.info()

# Correlation matrix 
def plot_correlation_matrix(data, columns, title="Correlation Matrix", cmap="coolwarm"):

    corr_matrix = data[columns].corr()
    
    # Plot the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap=cmap, fmt=".2f")
    plt.title(title)
    plt.show()

def time_series_plot(df, columns, timestamp_column='Timestamp'):
    # Plot Time series
    df[timestamp_column] = pd.to_datetime(df[timestamp_column])
    df.set_index(timestamp_column, inplace=True)
    df[columns].plot(figsize=(12, 6))
    plt.title("Time Series Plot")
    plt.xlabel("Timestamp")
    plt.ylabel("Values")
    plt.show()


def handle_missing_values(df, strategy='mean', columns=None):
    """
    Handles missing values in the dataframe.
    """
    if columns is None:
        columns = df.select_dtypes(include='number').columns
    
    if strategy == 'mean':
        df[columns] = df[columns].fillna(df[columns].mean())
    elif strategy == 'median':
        df[columns] = df[columns].fillna(df[columns].median())
    elif strategy == 'drop':
        df = df.dropna(subset=columns)
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', or 'drop'.")
    
    return df

def remove_outliers(df, column, threshold=3):
    """
    Removes outliers from a specified column using the Z-score method.
    """
    z_scores = (df[column] - df[column].mean()) / df[column].std()
    return df[z_scores.abs() <= threshold]
