# Countrywide Happiness as a Proxy of Food Security and Quality
**Concepts Applied:** Data Gathering, Data Cleaning/Scrubbing, Data Analysis, Data Visualization
**Language:** Python
**Libraries Used:** Numpy, Pandas, Seaborn, SQLite3, Plotly

## *TL;DR*
* As expected, the higher a country scores on the World Happiness Report, the higher it is likely to score in food security metrics (Overall security, affordability, availability, quality, and resilience of supply)
  * Correlation values of food security metrics and certain World Happiness Report variables (Score, GDP/capita, Social Support, and Healthy Life Expectancy) between 0.75-*0.95*, indicating a very strong relationship
  * Correlation values for other WHR variables (Freedom to Make Life Choices and Perceptions of Corruption was less impactful, however still signficant ranging from 0.35-0.5
* These findings are understood by further researcher exploring the political dogma and cultural attitudes/climates of countries in the analysis
  * Scandinavian countries score top ranks in happiness year after year due, in part, to their left-leaning politics allowing an expansive amount of freedoms to its citizens directly increasing perceived happiness. This secondarily affects food security as Finnish culture places an importance on wellbeing of the individual, leading to higher quality food and produce being subsidized and available. 
  * The inverse is true for countries that ranked low in the World Happiness Report; countries in sub-Saharan Africa scored low in metrics due to socioeconomic, historical, and civil hardships that are present after centuries of misuse and intentional wrongdoing. These hardships avert attention away from societal improvement and individual wellbeing to other, more vital causes such as infrastructure, subsidies for other sectors (ie. Industrial/Labor), and in some less fortunate cases, corruption; These decisions/actions contribute to lowering food security in the country substantially.

## Introduction 
This projects is an attempt to visualize the relationships between World Happiness Report scores and societal wellness metrics in the context of food security, specifically food afforability, availability, quality, and the resilience of the country's food supply, sourced from the Global Food Security Index. Data analysis and visualization was conducted in Jupyter Notebooks with Python 3 and its various libraries listed above.

* Data sourced from World Happiness Project and Global Food Security Index reports (2015-2019)
* Global Food Security Index tracks afforablilty, availability, quality and safety, and resilience of the food supply in a given country (https://foodsecurityindex.eiu.com/)
* World Happiness Project reports a generalized score after analyzing multiple key metrics such as societal freedom, GDP per capita, and more (https://worldhappiness.report/ed/2020/)
* Data was gathered from the websites linked above before being processed and cleaned with Pandas functions by me
* **From here on, the names of the reports will be shortened to WHR and GFSI respectively for simplicity

#### Data Gathering and Cleaning
Data was gathered as stated above in csv format and uploaded to a SQLite3 database as separate tables (WHR_2019, GFSI_2019, etc.) in a Jupyter Notebook. 
##### Notes
* Some csv files had to be encoded with `'latin-1'` to be uploaded
* Used SQL commands to query tables for verification of uploads
* Created a dataframe from a join between GFSI and WHR on GFSI's `Overall` column to keep similar countries between both tables (kept 108 distinct values, ie. countries)


## Exploratory Data Analysis
To begin my analysis I used Seaborn's heatmap function to create a correlation matrix to denote key trends and relationships. Shown below is the resulting graph, the key sections in it are marked. Key sections here refers to the sections of the graph that show true correlation between the GFSI and WHR, hence the areas outside of the boxes are not significant since they show recursive correlation between already linked variables contained within each table respectively.

#### Correlation Matrix
![Correlation Matrix](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/CorrelationMatrix2019.png)

<details>
<summary>Column Descriptions of Correlation Matrix</summary>
<ul><li>index = Index marker of GFSI and WHR reports, respectively </li>
<li>Placement = GFSI Placement; 1 is best</li>
<li>O_Score and its variates, such as Aff_Score and so on = Scores for food security metrics in a given country from GFSI (Overall, Affordability, Availability, Quality and Safety, and Natural Resources and Resilience)</li>
<li>Overall Rank and Score = WHR Placement; 1 is best</li>
<li>Social Support = From WHR; Amount of social support in a country based on policies and societal factors</li>
<li>Generosity and Perceptions of Corruption = Perceived rates of generosity or perceptions of corruption collected from polling citizens of a given country</li>
<li>The rest are self-explanatory</li></ul>
</details>


Seen within the key sections are two distinct areas, one of high correlation values and one of weaker, yet still significant, values. 
The former spans from the second `index` (index of WHR 2019) to `Healthy life expectancy`; the latter spans from `Freedom to make life choices` to `Perceptions of corruption` but does not include `Generosity`. These areas show positive correlation inciting further analysis into their relationships.

## Deep Dive
This is the deep dive text

