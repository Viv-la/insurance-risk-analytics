import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column, title):
    """
    Plot histogram distribution.
    """
    
    plt.figure(figsize=(10,6))
    
    sns.histplot(data[column], bins=30, kde=True)
    
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    
    plt.show()


def plot_boxplot(data, column, title):
    """
    Plot boxplot for outlier detection.
    """
    
    plt.figure(figsize=(10,6))
    
    sns.boxplot(x=data[column])
    
    plt.title(title)
    
    plt.show()