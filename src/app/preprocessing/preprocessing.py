'''
Main module for preprocessing.
'''
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

PATH = '../data/train.csv'

def encoding_values(df):
    '''
    encode categorical data to float
    Parameters:
        dataframe (pandas.DataFrame): DataFrame on which to operate
    Returns:
        pandas.DataFrame
    '''
    df_objects = (df.dtypes=='object')
    object_cols = list(df_objects[df_objects].index)
    ordinal_encoder = OrdinalEncoder()
    df[object_cols] = ordinal_encoder.fit_transform(df[object_cols])
    return df

def impute_values(df):
    '''
    Impute missing values in features
    Parameters:
        df (pandas.DataFrame): Dataframe on which to operate
    Returns:
        pandas.DataFrame
    '''
    imputer = SimpleImputer()
    imputer.fit(df)
    imputed_df = pd.DataFrame(imputer.transform(df))
    imputed_df.columns = df.columns
    return imputed_df

def scaling_values(df):
    '''
    Scaling features
    Parameters:
        df (pandas.DataFrame): Dataframe on which to operate
    Returns:
        pandas.DataFrame
    '''

    scaler = StandardScaler()
    x_train = df.drop(['Id', 'SalePrice'], axis=1)
    scaler.fit(x_train)
    scaled_data = scaler.transform(x_train)
    scaled_data = pd.DataFrame(scaled_data, columns=x_train.columns)
    scaled_data.insert(loc=0, column='Id', value=df['Id'])
    scaled_data['SalePrice'] = df['SalePrice']
    return scaled_data

def apply_preprocessing(df):
    '''
    Applying data cleaning functions to data sets
    Paramters:
        dataframe (pandas.DataFrame): Dataframe on which to operate
    Retruns:
        pandas.DataFrame
    '''
    df = encoding_values(df)
    df = scaling_values(df)
    df = impute_values(df)
    return df

def get_df():
    '''
    Sharing dataframe after aplying preprocessing
    Returns:
        pandas.DataFrame
    '''
    df = pd.read_csv(PATH)
    df = apply_preprocessing(df)
    return df
