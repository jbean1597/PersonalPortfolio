# Day 5: Visualize
## Objectives
* Calculate a variable for easy analysis and visualization across components
* Examine correlation between components and price
* Visualize relationship between variables and price

## Process
Within the spreadsheet, a step needs to be taken to create a column that can relate between components. This is done quickly in Google Sheets by creating a query where the entries/laptops are grouped by the components and calculating an average price column.
```
=query(A:N, "select B,D,E,G,H,I,AVG(L) group by B,D,E,G,H,I)
```
Once this is done, we have a table within the sheet that allows us to examine the relationships that components have on average price much easier. This data is then imported into Python to be visualized as a heatmap with Seaborn and Pandas.
![Heatmap of Components vs. Average Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Corr_heatmap1.png)

Next, in the spreadsheet, there were multiple graphs generated following the correlations found in the heatmap to explore further. The largest correlation coefficient was within the RAM column, followed by the SSD column, and thirdly by the GPU column. The largest largest inverse correlation was within the HDD column. Therefore, these columns are visualized first and reveal interesting insights.
![RAM Size vs Average Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/Ram's%20Effect%20on%20Price.png)
![SSD Size vs Average Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/SSD's%20Effect%20on%20Price.png)
![GPU Size vs Average Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/GPU's%20Effect%20on%20Price.png)

These graphs all show a positive relationship with average price - confirming the findings within the heatmap. What was almost more interesting though, is the relationship with HDD size.

#### Interesting Inverse Relationship with HDD Size
![HHD Size vs Average Price](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/YearInCode/Week1/img/HDD's%20Effect%20on%20Price.png)

