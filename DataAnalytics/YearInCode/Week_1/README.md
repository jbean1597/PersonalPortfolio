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

This dataset has null values, erroneously assigned variables("Missing" instead of null), wrong data types in columns (strings in columns that should be int/float), and duplicates.

The full, in-depth cleaning process can be found [here](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/Day_3.md)

## Day 4: Analyze
### Objectives
* Examine relationships between different variables and how they affect price
* Visulaize the relationships between variables, including brand name relationships

Once the data is cleaned, now the fun part begins where we can actually derive insights from our dataset. The full analysis process can be found [here](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/Day_4.md)

### Results
* RAM and SSD size had the largest impact on price, while CPU and GPU still affected price heavily the reasoning for it was due to the the increased prices of the top end processor series and GPU sizes (only being found in very expensive laptops)
  - HDD and display size showed little to no relationship (sometimes even being inversely related such as with HDD size)
* Apple did consistently charge much more - almost 2.5x more for the exact same components as other brands
* Dell, Acer, and ASUS were the opposite - consistently providing powerful and efficient budget laptops

### Key Takeaways for Your Next Shopping Trip
* Go with Apple for the M1/M2 chip and ecosystem
* Go for Dell, Acer, and ASUS for quality laptop brands then spend up from there for your needs


## Day 5: Visualize
### Objectives
* Calculate a variable for easy analysis and visualization across components
* Examine correlation between components and price
* Visualize relationship between variables and price

The full visualization process can be found [here](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/Day_5.md)

![Correlation Heatmap](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Corr_heatmap1.png)
### Positice Relationships
![Average Price by Brand](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Average%20Price%20by%20Brand.png)
![RAM Size and Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Ram's%20Effect%20on%20Price.png)
![SSD Size and Price](
https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/SSD's%20Effect%20on%20Price.png)
![GPU Size and Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/GPU's%20Effect%20on%20Price.png)

### Inverse or Interesting Relationships
![HDD Size and Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/HDD's%20Effect%20on%20Price.png)
![SSD & HDD Combo and Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/SSD_HDD%20Combo%20and%20Price%20(1).png)

## Day 6: Act
Since I am in the market for a new laptop (I have a 5 year old laptop that really struggles) I believe the insights from this will help me find the best laptop for my money. The way that will be accomplished is by using the insights gained from this analysis:
* RAM & SSD are the most expensive components 
* Brand plays a large role in price with some charging way more for the same components
* A combination of an HDD and an SSD is most of the time more affordable than *not* having an HDD

With this, I have narrowed down my choices to the ASUS ROG or the Dell Inspiron 15!

