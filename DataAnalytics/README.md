# Data Analytics and Visualization Projects
## About
I was introduced to coding my last year in university and since then have cultivated a deep interest in the science of data analysis and visualizations. This protfolio contains the projects I believe I did the best on and the ones that greatly improved my understanding of the material. I continue to practice the skills I have gained and am now focused on improving my machine/deep learning abilities. All of these projects were done in Python with the help of its libraries, such as Numpy, Pandas, Seaborn, Plotly, and SQLite3.

### Index
1. [Petrographic Analysis of High Porosity Rock Unit](https://github.com/jbean1597/PersonalPortfolio/tree/main/DataAnalytics/Petro_Analysis)
2. [Countrywide Happiness as a Proxy of Food Security](https://github.com/jbean1597/PersonalPortfolio/tree/main/DataAnalytics/Happiness_Analysis)


## Project 1: Petrographic Analysis of High Porosity Rock Unit
* Data collected, cleaned, and analyzed by me over the course of 2 years
* Analysis was carried out through Python, SQL, and Excel
* Rock unit was separated into 3 sections: Upper, Middle, and Lower
* Findings were compiled into an accessory quarterly report and presented to the project lead
* Resulting from this analysis, illite micro porosity was identified as a key factor in porosity levels, SEM analysis revealed the abundance of it and the crystal habit of the new illite variation found

### Correlation Matrix Heatmap from All Samples
This heatmap was the first visualization produced from the data after bringing it into an SQL database and loading it into Python. The green boxes are relationships we were expecting and were glad to find, the blue boxes are relationships that were anomalous and that I decided to do further analysis on.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/ALL%20TRM%20Correlation%20Matrix%20Seaborn.PNG)

#### Graph of Porosity vs. Depth
This graph shows the odd relationship present in this rock of porosity increasing as the depth increases. This is contrary to the normal relationship seen and was what really launched this project into the unit for carbon sequestration and research.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/PvD.PNG)

#### Total Cements vs. Porosity
Shown in this plot is the relationship of cement abundances in all the different units that were analyzed. Although the lower unit has similar levels of cements as the other units, it has much more porosity on average.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/CvP.PNG)

#### Intergranular Volume vs. Porosity
Finally, this plot explained a lot as the relationship between IGV and porosity has a limiting factor around 40% IGV. This is important since the abundance of illite in the samples collected barely ever went past 20%. With this info, the project then began using an SEM on specific samples used in this analysis and found a variation of illite present in the lower sections that has a large amount of micro porosity.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/IvP.PNG)

### Final Thoughts
This analysis began uncovering trends as soon as the EDA was conducted and led to a confirmation of the importance of illite in the diagenetic history of the rock unit. The report produced along with this was presented to the project lead and was a springboard for future analyses with both SEM and further point-counting. Micro porosity within the illite grains in the lower and middle sections due to a variation to their crystal habit is the cause of the differences in the porosity values seen between units; the lower and middle units contained the most of that variant and along with that had the highest porosity values.



## Project 2: Countrywide Happiness as a proxy of Food Security and Quality
* Data sourced from World Happiness Project and Global Food Security Index reports (2015-2019)
* Global Food Security Index tracks afforablilty, availability, quality and safety, and resilience of the food supply in a given country (https://foodsecurityindex.eiu.com/)
* World Happiness Project reports a generalized score after analyzing multiple key metrics such as societal freedom, GDP per capita, and more (https://worldhappiness.report/ed/2020/)
* Data was gathered from the websites linked above before being processed and cleaned with Pandas functions by me
* **Hypothesis:** Countries with higher scores in food security metrics will score higher in World Happiness Report score.

#### World Map of Reported Happines Report Scores 2019 (Higher is Better)
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/World_HappScore_2019.png)

#### High Correlation Between GDP/capita (bubble size), Affordability of Food, and Healthy Life Expectancy in 2019 by Region
Trends found after EDA with a correlation matrix in areas of high correlation were that there was a significant positive relationship between food security metrics and WHR scores. However, the most prevalent trend was that of GDP/capita which was consistently a marker for whether a country will score highly in food security metrics and/or WHR scores.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/Aff_HLE_GDP_bubble_2019.png)

#### Low Correlation (~0.45) Between Availability in Food Supply and Freedom to Make Life Choices
Correlation between availability in food supply and freedom to make life choices is weak, however the trend of GDP/capita present in the high correlation areas is present still. Hinting at a real significance between GDP/capita and overall wellbeing and report happiness scores.
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/AV_FMLC_GDP_bubble_2019.png)

### Final Thoughts
The analysis confirmed the hypothesis proposed and showed a very significant positive relationship between GDP/capita and overall wellbeing across multiple metrics, including all food security and World Happiness Report metrics. Even among relationships with low correlation values as shown above, GDP/capita is still a deciding factor in where a country places in the reports.




| Contact Me    | Links         |
| ------------- |:-------------:|
| email         | jakebean.geo@gmail.com |
| LinkedIn      | www.linkedin.com/in/jake-beangeo      |
