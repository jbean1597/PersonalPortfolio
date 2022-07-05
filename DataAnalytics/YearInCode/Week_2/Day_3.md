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
languages_df1 = languages_df.copy()
languages_df1.info()
```

This returns a dataframe of **32126 rows by 10 columns**. There are already some inconsistencies seen in the info section such as the ```Year``` column being an object instead of an ```int```.
### Null Values
Using 
```python
languages_df1.isnull().sum()
```
```python
Country or Area       0
Year                  0
Area                 86
Sex                  86
Language             86
Record Type          86
Reliability          86
Source Year          86
Value                86
Value Footnotes    9350
```
shows that 7/10 of the columns have 86 null values and the Value Footnotes column has 9350 null values. This is due to the Value Footnotes column not being necessary on some values since it is there to add description/classification to them. 


### Cleaning Data
Since the Value Footnotes data is a classification column I added a new classification for the null values. "0" is a new value for the rows which were null to signify a non-need for a classification. Along with that some columns needed to have their type changed to match the expected data type, such as the year column having a data type of object instead of int.
```python
languages_df1['Value Footnotes'] = languages_df1['Value Footnotes'].fillna(0)
languages_df1 = languages_df1.dropna()
languages_df1.isnull().sum()

```
```python
Country or Area    0
Year               0
Area               0
Sex                0
Language           0
Record Type        0
Reliability        0
Source Year        0
Value              0
Value Footnotes    0
```

To change the data type of the ```Year``` column, Panda's ```.astype()``` function is called.
```python
languages_df1['Year'] = languages_df1['Year'].astype('int')
```
```python
 0   Country or Area  32040 non-null  object 
 1   Year             32040 non-null  int32  
 2   Area             32040 non-null  object 
 3   Sex              32040 non-null  object 
 4   Language         32040 non-null  object 
 5   Record Type      32040 non-null  object 
 6   Reliability      32040 non-null  object 
 7   Source Year      32040 non-null  float64
 8   Value            32040 non-null  float64
 9   Value Footnotes  32040 non-null  object
```

### Dealing with Duplicates
This dataset is very well maintained in respect to duplicates. With
```python
languages_df1.duplicated().sum()
```
 we can see that there are no duplicates in the set. Concluding our cleaning and processing steps. The resulting dataset is **32040 rows by 10 columns**

