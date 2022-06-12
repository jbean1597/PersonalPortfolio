# Day 4: Analyze
## Objectives
* Examine relationships between different variables and how they affect price
* Visulaize the relationships between variables, including brand name relationships

Once the data is cleaned, it is exported out of the editor (VS Code) into a CSV file then uploaded into Google Sheets to perform the analysis and preliminary visualizations. This is done since the data set is small - only being 794 rows x 23 columns - and although Python/Pandas is very strong, it is unnecessary here and more lumbersome to use than a spreadsheet. 


## Results of Analysis
* TL;DR - The hypotheses (and common sense intuitions) proposed in the Ask phase were proven to be true based on the trends seen in the data
* Some interesting relationships were uncovered
  - Display size seemed to play a large role in affecting the price, however after further analysis it was shown that only a few data points (15.6", 14" 13.3") had more than 50 entries and they had an inverse relationship with a 15.6" screen having almost the same average price as a 14"
  - HDD size had a very interesting trend with the highest price on average being with a 512 GB HDD and the next highest being laptops with no HDD. The largest HDDs had the cheapest average prices
  - RAM size had an exponential relationship to price with a small increase between 4, 8, and 16 GB before an almost 2.5x increase from 16 GB to 32 GB
