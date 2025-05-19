import pandas as pd
import seaborn as sns

sns.set_theme(style="ticks")


def scatter_matrix(data: pd.DataFrame) -> None:
    """Plots a matrix of all correlations between data set attributes

    Args:
        data (pd.DataFrame): Data set
    """
    sns.pairplot(data)
    return
