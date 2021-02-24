# Petrographic Analysis of High Porosity Rock Unit in Illinois Basin
<br>**Concepts Applied:** Data Collection, Data Cleaning/Scrubbing, Accessing Database Tables, Data Analysis, Data Visualization</br>
<br>**Languages:** Python, SQL, Excel</br>
<br>**Libraries Used:** Numpy, Pandas, Seaborn, SQLite3</br>


## *TL;DR*
* Data used was collected completely manually by myself for the first year of the project, then an program-assisted method was used for the last year
* ~300 samples were collected (a roughly 20/80 mixture of whole core and rotary sidewall core samples respectively); Variables collected included depth, length of grains, sorting quality, and multiple calculated variables from mineralogical data within the samples themselves
* Project's focus was to establish a hypothesized connection between illite rims surrounding grains and an extraordinarily high porosity value seen in units in the Illinois Basin


### Findings at a Glance
Before the EDA was conducted it was thought that authigenic cements and depth were limiting factors in how porous a rock unit could be and it was generally found to be true. However, my analysis showed that this unit is anomolous since depth and porosity share a somewhat strong relationship which is further backed up by previous gamma ray log tests. Another interesting trend found was that IGV and total porosity were not as closely linked as we thought, producing a pearson coefficient of -0.25. This was explained later through SEM analysis of microporosity being vastly more abundant in this unit than in others, thanks largely due to the fibrosity of illite and other clay minerals present. This also explains why there is a large difference in the coefficients for total illite and total cements are so different; Other cements had no microporosity unlike illite.


#### Other Notable Findings
* The EDA defined multiple known relationships present in the data, such as grain size negatively affecting intergranular volume(IGV), authigenic illite abundance heavily linked to IGV, and Preliminary Primary Porosity being extremely dependent on sorting
* Contrary findings were present as well and were shown in the EDA to be of value for the project
* Graphs and visualizations were then produced with the data and presented to the project lead


## Introduction 
I conducted this analysis as a research project for the ISGS to examine a rock unit we found to have very high porosity. The financial incentive of the project was to use the rock unit as a carbon sequestration location for a large soybean and corn production plant, ADM. The unit was located in the Illinois Basin and was very thick in the core of the basin at close to 2000 feet. The data collected in this analysis was gathered manually by me with a point counter and a microscope for the first year of the project before we transferred to a much more efficient method of collection with the Petrog program. Once enough data was sufficiently collected, for this subgroup of 2 wells (6 in total) that was ~300 samples, I gathered it all into an excel sheet through Petrog and uploaded it into an SQL table before conducting EDA on the data through correlation matrices and later visualization in scatter plots.

#### Data Gathering and Cleaning
Data was gathered as stated above in Excel and then transferred into a CSV and upload into an SQL database. The data was then cleansed to remove non-necessary columns that printed out from the Petrog program. Finally, the data was cleansed to ensure no null values were present. 
##### Notes
* Data was also cleaned prior to transferring it to a CSV due to ease of implementation and need for accuracy in Excel
* Very few data points had null values; dataset was relatively clean, though contained too many columns at first

## Exploratory Data Analysis
Since this project was examining the relationship between variables present in this rock unit I decided a correlation matrix would be the best way to visualize a correlation between all the variables and identify important trends. Below is the correlation matrix produced from all the rotary sidewall cores(RSWC) and whole core(WC) samples in the wells. The green boxes correspond to relationships that I previously knew existed and were looking for while the blue boxes correspond with relationships we did not expect.

#### Correlation Matrices
<br>![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/ALL%20TRM%20Correlation%20Matrix%20Seaborn.PNG)
##### Fig. 1: Correlation Matrix of all samples from the wells
</br>
While looking at all the samples reveals overall trends from the entire dataset, the project was more interested in 2 sections specifically, the middle and the lower units. The most porous and thickest rock unit were in these and they were the primary area where the carbon sequestration would take place. Given that, I could quickly produce heatmaps for both these units. 

![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/TRM%20Middle%20Correlation%20Matrix%20Seaborn.PNG)
##### Fig. 2: Correlation Matrix of samples from middle section of unit

![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/TRM%20Lower%20Correlation%20Matrix%20Seaborn.PNG)
##### Fig. 3: Correlation Matrix of samples from lower section of unit


