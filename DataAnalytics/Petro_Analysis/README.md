# Petrographic Analysis of High Porosity Rock Unit in Illinois Basin
<br>**Concepts Applied:** Data Collection, Data Cleaning/Scrubbing, Accessing Database Tables, Data Analysis, Data Visualization</br>
<br>**Languages:** Python, SQL, Excel</br>
<br>**Libraries Used:** Numpy, Pandas, Seaborn, SQLite3</br>


## *TL;DR*
* Data used was collected completely manually by myself for the first year of the project, then an program-assisted method was used for the last year
* ~200 samples were collected (a roughly 20/80 mixture of whole core and rotary sidewall core samples respectively); Variables collected included depth, length of grains, sorting quality, and multiple calculated variables from mineralogical data within the samples themselves
* Project's focus was to establish a hypothesized connection between illite rims surrounding grains and an extraordinarily high porosity value seen in units in the Illinois Basin


### Findings at a Glance
Before the EDA was conducted it was thought that authigenic cements and depth were limiting factors in how porous a rock unit could be and it was generally found to be true. However, my analysis showed that this unit is anomolous since depth and porosity share a somewhat strong relationship which is further backed up by previous gamma ray log tests. Another interesting trend found was that IGV and total porosity were not as closely linked as we thought, producing a pearson coefficient value of ~0.25. This was explained later through SEM analysis of microporosity being vastly more abundant in this unit than in others, thanks largely due to the fibrosity of illite and other clay minerals present. This also explains why there is a large difference in the coefficients for total illite and total cements are so different; Other cements had no microporosity unlike illite.


#### Other Notable Findings
* The EDA defined multiple known relationships present in the data, such as grain size negatively affecting intergranular volume(IGV) and Preliminary Primary Porosity being extremely dependent on sorting
* Contrary findings were present as well and were shown in the EDA to be of value for the project
* Graphs and visualizations were then produced with the data and presented to the project lead


## Introduction 
I conducted this analysis as a research project for the ISGS to examine a rock unit we found to have very high porosity. The financial incentive of the project was to use the rock unit as a carbon sequestration location for a large soybean and corn production plant, ADM. The data collected in this analysis was gathered manually by me with a point counter and a microscope for the first year of the project before we transferred to a much more efficient method of collection with the Petrog program. Once enough data was sufficiently collected, for this subgroup of 2 wells (6 in total) that was ~200 samples, I gathered it all into an excel sheet through Petrog and uploaded it into an SQL table before conducting EDA on the data through correlation matrices and later visualization in scatter plots.

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
The same trends were generally seen in the middle and lower section and after presenting the finding to the my boss, the project lead, I decided to visualize the data in Excel due to the data already being in an excel file. 

## Further Analysis
The visualizations I did in Excel were of 5 graphs with porosity and 6 graphs with depth, both against a variety of variables. The project lead wanted the RSWC and WC samples to be separated and visualized in their own graphs so in total there were 22 graphs produced from this data. Below will be a sample of the most impactful visualizations with explanations why they were important.
<br>
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/CvP.PNG)
##### Fig. 4: Total Cements vs. Porosity
This graph was produced to see the relationships of cements and porosity in each unit. It shows that the lower unit specifically has much more porosity even though it has a similar amount of cements as all the other units. This was the first to spark interest into studying the specific cements further in a SEM microscope. 
</br>
<br>
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/IllvP.PNG)
##### Fig. 5: Total Illite vs. Porosity
This graph further exemplified the trends found in figure 4 but with a focus on illite in the samples. Along with this graph, the other cements were also graphed and they showed much more variation and little to no correlation, exactly as seen in the correlation matrix.
</br>
<br>
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/IvP.PNG)
##### Fig. 6: IGV vs. Porosity
At this point the story began to come together with the visualization of intergranular volume and porosity. It shows a limiting factor in the porosity of the sample that we had not seen before, a sharp drop-off in porosity when IGV passes 40%. This is odd since IGV inherently includes porosity in its calculation of the *entire* volume of the rock minus the grain volume. This was explored later and was due to the samples with more than 40% IGV were within the Argenta and Eau Claire, two units with little to no porosity and cements filling every pore. This graph shows the point for the maximum amount of porosity with respect to IGV is found between 25-40% iGV and can climb as high as 30% porosity, an extremely high value that you would never expect to find more than 6000 feet below the surface.
</br>
<br>
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/IvD.png)
##### Fig. 7: Total Illite vs. Depth
This graph again shows the lack of distinction in illite abundances between the units. There is little to no variation with only a few outliers.
</br>
<br>
![](https://github.com/jbean1597/PersonalPortfolio/blob/main/DataAnalytics/Petro_Analysis/images/PvD.PNG)
##### Fig. 8: Porosity vs. Depth
The inverse relationship between porosity and depth was seen in this graph along with a clear distinction betweeen the rock units in an easy to understand way. The porosity increases as you go deeper, contrary to what is normal.
</br>


