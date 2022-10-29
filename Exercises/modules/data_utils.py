import pandas as pd
import seaborn as sns

def columns_with_nans(df: pd.DataFrame) -> sns.barplot:
    """Takes a dataframe and plots NaN counts of columns with any NaN"""
    na_cols = df.loc[:, df.isna().any(axis=0)]
    na_df = pd.DataFrame({"Columns": list(na_cols.columns), "NaN": list(na_cols.isna().sum())})
    sns.barplot(na_df, x="Columns", y = "NaN")