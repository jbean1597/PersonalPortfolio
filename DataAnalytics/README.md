# Data Analytics and Visualization Projects
## About
I was introduced to coding my last year in university and since then have cultivated a deep interest in the science of data analysis and visualizations. This protfolio contains the projects I believe I did the best on and the ones that greatly improved my understanding of the material. I continue to practice the skills I have gained and am now focused on improving my machine/deep learning abilities. All of these projects were done in Python with the help of its libraries, such as Numpy, Pandas, Seaborn, Plotly, and SQLite3.

### Index
1. [Petrographic Analysis of High Porosity Rock Unit]()
2. [Countrywide Happiness as a Proxy of Food Security](https://github.com/jbean1597/PersonalPortfolio/tree/main/DataAnalytics/Happiness_Analysis)


## Project 1: Countrywide Happiness as a proxy of Food Security and Quality
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
