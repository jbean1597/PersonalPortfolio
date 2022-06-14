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
![Heatmap of Components vs. Average Price]()

Next, in the spreadsheet, there were multiple graphs generated following the correlations found in the heatmap to explore further. The largest correlation coefficient was within the RAM column, followed by the SSD column, and thirdly by the GPU column. The largest largest inverse correlation was within the HDD column. Therefore, these columns are visualized first and reveal interesting insights.
![RAM Size vs Average Price]()
![SSD Size vs Average Price]()
![GPU Size vs Average Price]()
![HHD Size vs Average Price]()
