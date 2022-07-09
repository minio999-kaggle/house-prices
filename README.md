# house-prices predictions
House Prices Regression [Kaggle competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.

## Credits
* Maciej Bialoglowski  ([@chemista](https://github.com/chemista))

## Method
Below are provided steps that I followed for this Project.

### 1. **Data visualization**: Data analisys to understand features, missing values, mean values (for further use) and other usefull information.
- Understanding features (There are 79 of them I will list there most important)
    - **SalePrice** - the property's sale price in dollars. This is the target variable that you're trying to predict.
    - **LotFrontage**: Linear feet of street connected to property
    - **LotArea**: Lot size in square feet
    - **LotShape**: General shape of property
    - **OverallQual**: Overall material and finish quality
    - **OverallCond**: Overall condition rating
    - **YearBuilt**: Original construction date
    - **ExterQual**: Exterior material quality
    - **ExterCond**: Present condition of the material on the exterior
    - **Heating**: Type of heating
    - **CentralAir**: Central air conditioning
    - **Electrical**: Electrical system
    - **Bedroom**: Number of bedrooms above basement level
    - **Kitchen**: Number of kitchens
    - **GarageCars**: Size of garage in car capacity
- Looking out for null values
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/preproccesing1.ipynb))

- Getting better knowlage about data
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/preproccesing1.ipynb))

- Conclusion
We can see that there are some features which have too much null values to care about them. There are some outliers as well. A lot of object types columns which we want to encode.

### 2. **Preprocessing**: with the knowledge acquired with data visualization, we can apply it to dealing with missing values and categorical data.

- Encoding Features
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/preproccesing1.ipynb))
- Imputing Values
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/preproccesing1.ipynb))
- Scaling Features
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/robust_scaler.ipynb))
- Aplying Preproccesing to data (Refactoring)
([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/preproccesing1.ipynb))
- Cross-Validation
It is used everytime I am training model.

### 3. **Model Selection**: choosing model based on mse scores
- After all catboost was the best ([Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/model_selection.ipynb))

### 4. **Model Tuning**: Hyperparameter model 
[Jupyters notebook](https://github.com/minio999-kaggle/house-prices/blob/dev/playground/modeltuning.ipynb)

## Folder Structures
* `\` contains all of setup files
* `\data` contains data
* `\src\app` contains code
* `\src\app\preprocessing` contains code used for preprocessing methods
* `\playground` contains jupyter notebooks for test purpose
* `\tests` contains test

## Installation instructions
1. Install Python and clone this repository
2. Open files, find cloned repository, open terminal inside that folder and use command `./run.sh`

to run the [jupyter](http://jupyter.org/)'s notebooks or mess with it yourself download docker, open powershell and run `.\jupyter-start.ps1`
