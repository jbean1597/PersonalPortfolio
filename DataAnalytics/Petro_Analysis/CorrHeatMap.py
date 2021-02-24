import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data = { 'Depth': [],
         'Mean Length': [],
         'Std Dev': [],
         'Sorting': [],
         'PrePrimPorosity': [],
         'Porosity Loss': [],
         'IGV': [],
         'Total Illite': [],
         'Total AuthQ': [],
         'Total Cements': [],
         'Total Porosity': []
         }

df = pd.DataFrame(data,columns=['Depth','Mean Length','Std Dev','Sorting','PrePrimPorosity','Porosity Loss','IGV','Total Illite','Total AuthQ','Total Cements','Total Porosity'])
corrMatrixAll = df.corr()
print(corrMatrixAll)

plt.subplots(figsize=(20,15))
heat_map = sb.heatmap(corrMatrixAll, annot=True)
heat_map.set_yticklabels(heat_map.get_yticklabels(), rotation=0)
bottom, top = heat_map.get_ylim()
heat_map.set_ylim(bottom + 0.5, top - 0.5)
plt.show()