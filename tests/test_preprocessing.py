import numpy as np
import pandas as pd
from app.preprocessing import apply_preprocessing

def test_transorm_data():
    """
    Test apply_preprocessing function
    """
    test_data = {'Id': [1, 2, 3, 4, 5],
                'test': [1,np.nan,3,np.nan,5],
                'category': ['a','b',np.nan,'d','e'],
                'SalePrice': [12334, 200000, 43222, 124124, 123442]}
    df = pd.DataFrame(test_data)
    df = apply_preprocessing(df)
    df = df.round(decimals=5)
    expected_df = pd.DataFrame({'Id': [1.0, 2.0, 3.0, 4.0, 5.0],
                        'test': [-1.58114, 0.00000, 0.00000, 0.00000, 1.58114],
                        'category': [-1.5, -0.5, 0.0, 0.5, 1.5],
                        'SalePrice': [12334.0, 200000.0, 43222.0, 124124.0, 123442.0]})
    assert df.equals(expected_df)