# Week 1: Laptop Prices By Components and Other Metrics
### Data
* Source: Kaggle 
  - [2022 March Laptop data](https://www.kaggle.com/datasets/kuchhbhi/2022-march-laptop-data)


## The Problem
Laptop prices seem to rise every day and with the sheer amount of models and different components within them, it's almost impossible to discern which model with what components is the best bang for your buck. This project will explore the data and see what insights can be taken to help make the best decison. 

## Day 1: Ask
* What component has the greatest effect on price?
* What component has the least effect on price?
* Do some brands charge more for the same components?
* Is there a brand that consistently charges lower for the same components making it a great option for a budget brand? 
* **Hypotheses:** Apple will consistently be a higher price for the same components and the CPU or GPU will have the largest effect on price

## Day 2: Prepare
* What data needs to be collected and where will it come from?
  - Laptop prices, brands, and components. The data comes from scraped data collected by the author of the Kaggle dataset, Santosh Kuma.
* Where is the data located?
  - The data was dowloaded from Kaggle and is stored internally.
* What needs to be figured out and how will it be done?
  - Relationships between price and the other variables, i.e. price vs. processor, price vs. brand, etc.
  - Relationships will be found through correlation matrices and analysis.

## Day 3: Process
### Objectives
* Clean data of null values (25 rows have nulls)
* Examine datatypes for inconsistencies 
* Remove duplicates
* Verify that each column has consistent format

First we import the data and create a copy of the DataFrame so we can retain the original in the case that we need to recover the original data.
```python
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df_laptop = pd.read_csv(r'C:\Users\jbean\OneDrive\Desktop\Portfolio_Projects\Year_In_Code\Week_1_Laptop\Week_1_Data\Cleaned_Laptop_data.csv')
df_laptop_modified = df_laptop.copy() 
```
The resulting DataFrame is 896 rows x 23 columns

##### Null Values
```python
df = df_laptop_modified.dropna()
```
This removes 25 rows from the DataFrame - all null values were within the ram_gb column, found by using:
```python
df['ram_gb'].isnull().sum()
```

##### Consistency Issues
After the null values were taken care of, there was still a problem with inconsistent and wrong datatypes in the DataFrame. Using:
```python
df.info()
```
it is seen that the columns ram_gb and display_size are classified as objects when they should be integers/floats.

This requires some further exploration so calling the unique() command on each row we can see why it is classified as such. The ram_gb column contains a mix of integers and brand/type of ram names; the display_size column contains values that don't make any sense such as 'All', '6th', '8th', 'ITW', '0'. 

This is remedied by using the following code which removes the incorrect values and switches the type to int and float respectively:
```python
df = df[~df['ram_gb'].str.contains('|'.join(drop_ram_values))]
df['ram_gb'] = df['ram_gb'].astype(str).astype(int)
df = df[~df['display_size'].str.contains('|'.join(drop_display_values))]
df['display_size'] = df['display_size'].astype(str).astype(float)
```

##### Duplicates
With:
```python
df.duplicated().sum()
```
We see that there are 22 duplicates in the DataFrame. Removing them with 
```python
df = df.drop_duplicates(keep='first')
``` 
returns our fully cleaned and ready to use DataFrame of 849 rows by 23 columns.
