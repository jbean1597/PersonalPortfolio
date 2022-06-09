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

