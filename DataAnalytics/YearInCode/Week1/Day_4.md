# Day 4: Analyze
## Objectives
* Examine relationships between different variables and how they affect price
* Visulaize the relationships between variables, including brand name relationships

Once the data is cleaned, it is exported out of the editor (VS Code) into a CSV file then uploaded into Google Sheets to perform the analysis and preliminary visualizations. This is done since the data set is small - only being 794 rows x 23 columns - and although Python/Pandas is very strong, it is unnecessary here and more lumbersome to use than a spreadsheet. 


## Results of Analysis
#### TL;DR 

* The hypotheses (and common sense intuitions) proposed in the Ask phase were proven to be true based on the trends seen in the data but were more complex than just singular components being the most influential on price
* Some interesting relationships were uncovered
  - Display size seemed to play a large role in affecting the price, however after further analysis it was shown that only a few data points (15.6", 14" 13.3") had more than 50 entries and they had an inverse relationship with a 15.6" screen having almost the same average price as a 14"
  - HDD size had a very interesting trend with the highest price on average being with a 512GB HDD and the next highest being laptops with no HDD. The largest HDDs had the cheapest average prices
  - RAM size had an exponential relationship to price with a small increase between 4, 8, and 16GB before an almost 2.5x increase from 16GB to 32GB

### Deep Dive into the Data
#### Singular Components With The Most/Least Effect on Price
##### Most (in order of influence)
* RAM Size
* SSD Size
* GPU Size

##### Least (in order of influence)
* Display Size
* HDD Size
* Processor Series (except for top of the line processor series like the M1, Core i9, and Ryzen 9 chips)

#### Final Results
While there were certainly components that had a larger impact on the overall price, the complete story is one of needing to consider multiple variables.  Overall, RAM and SSD size had a similar positive relationship to price, GPU also sharing that relationship to a slightly lesser amount. Display size had almost no correlation to price along with HDD size. 

##### Hypotheses Answers 
Apple was shown to consistently charge substantially more for the same or lesser componenets (pretty obvious) however, that price might be justified when taking into account the M1 and upcoming M2 powerhouse chips along with the Apple ecosystem. The next part of the hypothesis, that CPU and GPU would have the largest effect on price was true - only for the top end products. GPUs below 6GB had minimal effect on price and were relatively cost effective especially considering the power a GPU grants. The components that actually affected price most were the SSD and RAM size, which makes sense given the cost of the components on their own.


