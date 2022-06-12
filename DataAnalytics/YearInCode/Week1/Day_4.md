# Day 4: Analyze
## Objectives
* Examine relationships between different variables and how they affect price
* Visulaize the relationships between variables, including brand name relationships

Once the data is cleaned, it is exported out of the editor (VS Code) into a CSV file then uploaded into Google Sheets to perform the analysis and preliminary visualizations. This is done since the data set is small - only being 794 rows x 23 columns - and although Python/Pandas is very strong, it is unnecessary here and more lumbersome to use than a spreadsheet. 


## Results of Analysis
### TL;DR 
* The hypotheses (and common sense intuitions) proposed in the Ask phase were proven to be true based on the trends seen in the data but were more complex than just singular components being the most influential on price
* Apple (to no surpise) was consistently shown to be charging about 2.5x more for their laptops as the next closest competitor - making them the most expensive laptop by far, sometimes being 2x more expensive than laptops with better components
* Some interesting relationships were uncovered
  - Display size seemed to play a large role in affecting the price, however after further analysis it was shown that only a few data points (15.6", 14" 13.3") had more than 50 entries and they had an inverse relationship with a 15.6" screen having almost the same average price as a 14"
  - HDD size had a very interesting trend with the highest price on average being with a 512GB HDD and the next highest being laptops with no HDD. The largest HDDs had the cheapest average prices
  - RAM size had an exponential relationship to price with a small increase between 4, 8, and 16GB before an almost 2.5x increase from 16GB to 32GB

![Apple Leading the Pack](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Average%20Price%20by%20Brand.png)

#### The Best Laptop Under $1000 (Student/Budget Laptop)
The ASUS ROG and Dell Inspiron 15 laptops offer a lot of power for a relatively low cost. They both have a 1TB SSD drive and 8GB of ram. The ASUS ROG has a 4GB GPU and a Ryzen 7 CPU, pushing it to compete with higher cost laptop for hundreds less at **$948.87**. The Dell Inspiron 15 has a Ryzen 5 CPU with integrated Radeon GPU, coming in at only **$752.70**

#### The Best Bang for Your Buck (Perfect for Data Analysts)
The Lenovo IdeaPad 5 has an incredibly strong lineup for just barely over $1000. With a 1TB HDD and 512GB SSD drive paired with a Ryzen 7 and 16GB of RAM, there's no task (other than high quality video editing/rendering) that it can't do with ease. 

#### Mr. Money Bags (The Most Powerful Laptops)
First up, congrats if you can buy any of these - the price tags are almost getting into used car territory. The 2021 Apple Pro (**$4029.87**) with the incredibly powerful M1 Max chip is the crowd favorite here, it has all the bells and whistles including 1TB SSD, 32GB RAM, along with the increased efficiency from the M1 architecture. Next is a *budget* version of our final laptop - the ASUS ROG with 1TB SSD, 32GB of RAM, Ryzen 9, and (the true differentiator) a 4GB GPU all for *only* **$2179.54**. Finally, if you have money to blow and want the absolute best machine money can buy then you'd be more than happy with the ASUS Zephyrus. Sporting a 3TB SSD, Intel Core i9 CPU, 32GB of RAM, and a whopping 6GB GPU there's no doubt it is one of the most powerful laptops out there. You only need the equivalent to a down payment on a mansion in Texas, a cool **$5745.87**. 


## Deep Dive into the Data
![Correlation Heatmap](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Corr_heatmap.png)

### Singular Components With The Most/Least Effect on Price
#### Most (in order of influence)
* RAM Size
* SSD Size
* GPU Size

![RAM Size vs. Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Ram's%20Effect%20on%20Price.png)

#### Least (in order of influence)
* Display Size
* HDD Size
* Processor Series (except for top of the line processor series like the M1, Core i9, and Ryzen 9 chips)

![HDD Size vs. Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/HDD's%20Effect%20on%20Price.png)

### Final Results
While there were certainly components that had a larger impact on the overall price, the complete story is one of needing to consider multiple variables.  Overall, RAM and SSD size had a similar positive relationship to price, GPU also sharing that relationship to a slightly lesser amount. Display size had almost no correlation to price along with HDD size. The lack of correlation in HDD size is likely due to the relationship that it has with SSD size, most laptops will combine the two storage systems but the effect/price of SSD drives is much higher than the HDD's effect.

#### Hypotheses Answers 
Apple was shown to consistently charge substantially more for the same or lesser componenets (pretty obvious) however, that price might be justified when taking into account the M1 and upcoming M2 powerhouse chips along with the Apple ecosystem. The next part of the hypothesis, that CPU and GPU would have the largest effect on price was true - only for the top end products. GPUs below 6GB had minimal effect on price and were relatively cost effective especially considering the power a GPU grants. The components that actually affected price most were the SSD and RAM size, which makes sense given the cost of the components on their own.


