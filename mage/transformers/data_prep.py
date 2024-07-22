import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def prepare_data(df):
    """
    Prepare data by removing the target column.
    """
    target_column="fraud"
    # Cut the dataset to 500 to reduce time for this project
    # the actual practice should be making prediction script receive batch/chunk data to increase performance
    # Or making a parallel processing to increase performance but we will leave the idea here
    df_cut = df.head(5)

    return df_cut[target_column], df_cut.drop(columns=[target_column])
