import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

sb.set_style('darkgrid')
sb.set_context('paper')

# loading data
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Bathy.csv")
dfM.head(5)

# plotting
sb.catplot(
           data=dfM, kind="violin", scale='count', palette="Paired",
           orient="v", legend=True, legend_out=True,
           margin_titles=True, linewidth=0.2
           )
plt.xticks(rotation=45)
plt.title('Violin plots for the Mariana Trench bathymetry',
          fontsize=12, fontfamily='serif')
plt.subplots_adjust(bottom=0.15,top=0.85)

# visualizing
plt.tight_layout()
plt.savefig('plot_Hist.png', dpi=300)
plt.show()
