# Countrywide Happiness as a Proxy of Food Security and Quality
<br>**Concepts Applied:** Data Gathering, Data Cleaning/Scrubbing, Accessing Database Tables, Data Analysis, Data Visualization</br>
<br>**Languages:** Python and SQL</br>
<br>**Libraries Used:** Numpy, Pandas, Seaborn, SQLite3, Plotly</br>


## *TL;DR*
* EDA and follow up analysis of World Happiness Report scores and Global Food Security metrics
* Goal: Identify and visualize relationships between the two reports and verify hypothesis
* Hypothesis: Countries with a higher World Happiness Report score will have a better score on the food security metrics outlined in this report (overall, affordability, availability, quality and safety, natural resources and resilience)


### Findings at a Glance
* As expected, the higher a country scores on the World Happiness Report, the higher it is likely to score in food security metrics (Overall security, affordability, availability, quality, and resilience of supply)
  * Strong correlation between food security metrics and certain World Happiness Report variables (Score, GDP/capita, Social Support, and Healthy Life Expectancy); values between 0.75-**0.95**
  * Weaker correlation between other WHR variables (Freedom to Make Life Choices and Perceptions of Corruption) was less impactful, however still signficant ranging from 0.35-0.5
* These findings are understood by further researcher exploring the political dogma and cultural attitudes/climates of countries in the analysis
  * Scandinavian countries score top ranks in happiness year after year due, in part, to their left-leaning politics allowing an expansive amount of freedoms to its citizens directly increasing perceived happiness. This secondarily affects food security as Finnish culture places an importance on wellbeing of the individual, leading to higher quality food and produce being subsidized and  widely available.  
  * The inverse is true for countries that ranked low in the World Happiness Report; countries in sub-Saharan Africa scored low in metrics due to socioeconomic, historical, and civil hardships that are present after centuries of volatility. These hardships avert attention away from societal improvement and individual wellbeing to other, more vital causes such as infrastructure, subsidies for other sectors (ie. Industrial/Labor), and in some less fortunate cases, corruption; These decisions/actions contribute to lowering food security in the country substantially.
* These findings are simplified representations of complex, multi-level political, economic, and societal schema and as such they should not be used in predictive analyses. Their use is bound to classification, verification, and linear analyses of trends due to their simplicity.

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
* Some csv files had to be encoded with `encoding='latin-1'` to be uploaded
* Used SQL commands to query tables for verification of uploads
* Created dataframe from a join between GFSI and WHR on GFSI's `Overall` column to keep similar countries between both tables (kept 108 distinct values, ie. countries)


## Exploratory Data Analysis
To begin my analysis I used Seaborn's heatmap function to create a correlation matrix to denote key trends and relationships. Shown below is the resulting graph. Key sections of the graph are those that show true correlation between the GFSI and WHR, such as the values contained within the red boxes. Values outside of these boxes are not significant since they show recursive correlation between already linked variables contained within each table respectively.

#### Correlation Matrix
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/CorrelationMatrix2019.png)

<details>
<summary>Column Descriptions of Correlation Matrix</summary>
<ul><li>index = Index marker of GFSI and WHR reports, respectively </li>
<li>Placement = GFSI Placement; 1 is best</li>
<li>O_Score and its variates, such as Aff_Score and so on = Scores for food security metrics in a given country from GFSI (Overall, Affordability, Availability, Quality and Safety, and Natural Resources and Resilience)</li>
<li>Overall Rank and Score = WHR Placement; 1 is best</li>
<li>Social Support = From WHR; Amount of social support in a country based on policies and societal factors</li>
<li>Generosity and Perceptions of Corruption = Perceived rates of generosity or perceptions of corruption collected from polling citizens of a given country</li>
<li>The rest not named here are self-explanatory</li></ul>
</details>


Seen within the key sections are two distinct areas, one of high correlation values and one of weaker, yet still significant, values. `Generosity` is not included as it has no significant correlation. After examining all other correlation matrices (2015-2018), the pattern was found in all of them in high confidence with almost identical bounds and values.

Other areas of interest could be the highly negative correlation of the first two columns of the key section, however, these are easily exlpained by the nature of the index and placement numbering. Index begins at 0 as increases incrementally with each row, whereas the scores decrease as the placement gets lower.


|Correlation      | Value Range          | Starting Column  | Ending Column |
| ------------- |:-------------:|:-----:|:-----:|
| STRONG     | 0.75-0.95 | `index` | `Healthy life expectancy` |
| WEAK      | 0.35-0.5      | `Freedom to make life choices` | `Perceptions of corruption` |

#### World Map of World Happiness Report Scores
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/World_HappScore_2019.png)
 
 ##### Table of top 5 countries by WHR scores
|Placement    | Country          | Score | 
| ------------- |:-------------:|:-----:|
| 1    | Finlane | 7.769 |
| 2    | Denmark     | 7.600 |
| 3    | Norway      | 7.554 |
| 4    | Iceland      | 7.494 |
| 5    | Netherlands      | 7.488 |
## Final Analyses
#### Important Notes
* GDP/capita is one of the most consistently, strongly correlated variables so it will be included in almost every analysis
 * Bubble analyses will be used for their ease-of-representation of this variable

### High Correlation Area
Within the two defined areas there are certain areas that are more interesting to verify, such as quality and safety of the food supply and the healthy life expectancy of a given country. Below is a bubble chart of just that correlation with GDP/capita as the size of the bubbles. Supporting the hypothesis, there is a clear positive trend between GDP/capita, healthy life expectancy, and quality and safety of the food supply; As one variable increases, the others are likely to do so as well. Another aspect to notice is the decrease in variance the more affluent and higher quality of life a country is. This is due to the obvious fact that the amount of hardships is minimized in developed countries and conversely, in developing countries there are a varyng ranges of hardships that affect countries up to a certain GDP/capita and Quality and Safety score. 
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/QS_HLE_GDP_bubble_2019.png)

The same trend is repeated through all variations of food security metrics compared to WHR columns in the high correlation group. Shown below is another example of the trend seen through all years with affordability scores compared to reported happiness scores. 
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Happiness_Analysis/images/Aff_Score_GDP_bubble_2019.png)

### Low Correlation Area

