import numpy as np
import pandas as pd
from app.preprocessing import apply_preprocessing

def test_apply_preprocessing():
    """
    Test apply_preprocessing function
    """
    test_data = {'Id': [1, 2, 3, 4, 5],
                'Alley': ['null', 'Pave', 'Grvl', 'Pave', 'Grvl'],
                'PoolQC': ['null', 'Ex', 'Gd', 'TA', 'Ex'],
                'Fence': ['null', 'MnWw', 'GdWo', 'MnWw', 'GdWo'],
                'MiscFeature': ['null', 'Elev', 'Gar2', 'Shed', 'Elev'],
                'test': [1,np.nan,3,np.nan,5],
                'category': ['a','b',np.nan,'d','e'],
                'SalePrice': [12334, 200000, 43222, 124124, 123442]}
    df = pd.DataFrame(test_data)
    df = apply_preprocessing(df)
    df = df.round(decimals=5)
    expected_df = pd.DataFrame({'Id': [1.0, 2.0, 3.0, 4.0, 5.0],
                        'test': [-2.0, 0.0, 0.0, 0.0, 2.0],
                        'category': [-1.5, -0.5, 0.0, 0.5, 1.5],
                        'SalePrice': [12334.0, 200000.0, 43222.0, 124124.0, 123442.0]})
    assert df.equals(expected_df)