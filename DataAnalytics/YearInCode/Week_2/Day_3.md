# Day 3: Process
## Objectives
* Clean data and establish a framework for what to remove/clean and what shouldn't be affected
* Remove null values
* Standardize some values in the datasets for easier analysis

First the data is imported into a Jupyter Notebook to process and clean using the kernels function. ```.info()``` is used to give a preliminary overvview of the dataset.

```python
import pandas as pd
import numpy as np
import os

languages_df = pd.read_csv(r'C:\Users\jbean\OneDrive\Desktop\Portfolio_Projects\Year_In_Code\Week_2_Languages\Week_2_Data\raw_UNdata_languages.csv')
languages_df.info()
```

This returns a dataframe of **32126 rows by 10 columns**. There are already some inconsistencies seen in the info section such as the ```Year``` column being an object instead of an ```int```.
### Null Values
Using 
```python
languages_df.isnull().sum()
```
shows that 7/10 of the columns have 86 null values and the Value Footnotes column has 9350 null values. This is due to the Value Footnotes column not being necessary on some values since it is there to add description/classification to them. 


### Cleaning Data
Since the Value Footnotes data is a classification column I added a new classification for the null values. "0" is a new value for the rows which were null to signify a non-need for a classification. Along with that some columns needed to have their type changed to match the expected data type, such as the year column having a data type of object instead of int.