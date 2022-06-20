# Day 3: Process
## Objectives
* Clean data and establish a framework for what to remove/clean and what shouldn't be affected
* Remove null values
* Standardize some values in the datasets for easier analysis

First the data is imported into a Jupyter Notebook to process and clean using the kernels function. ```python .info()``` is used to give a preliminary overvview of the dataset.

```python
import pandas as pd
import numpy as np
import os

languages_df = pd.read_csv(r'C:\Users\jbean\OneDrive\Desktop\Portfolio_Projects\Year_In_Code\Week_2_Languages\Week_2_Data\raw_UNdata_languages.csv')
languages_df.info()
```
