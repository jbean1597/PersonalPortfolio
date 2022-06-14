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
Once this is done, we have a table within the sheet that allows us to examine the relationships that components have on average price much easier. 
