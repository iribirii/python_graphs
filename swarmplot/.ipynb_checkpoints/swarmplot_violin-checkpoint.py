import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_sqa = pd.read_csv('sqa_data.csv')

swarmplot_palette = {'Sqa_par':'#8f96bf', 'Sqa_bif':'#ebb0e5', 'Sqa_zz':'#9feed3'}
violin_palette = {'Sqa_par':'#333c70', 'Sqa_bif':'#90367c', 'Sqa_zz':'#34906c'}

sns.set_context('talk', font_scale=1)

plt.figure(figsize=(14,6))
sns.violinplot(y="dist", 
               x="name", 
               data=df_sqa,
               palette=violin_palette,
               scale='count',
               inner=None
              )

sns.swarmplot(y="dist",
              x="name",
              data=df_sqa, 
              color="white", 
              edgecolor="gray",
              s=8,
              palette=swarmplot_palette
             )

plt.xticks([0, 1, 2], ['parallel','bifurcated','zig-zag'])
plt.xlabel('squaramide CCSD systems')
plt.ylabel(r'$distance\ (\AA)$')
plt.tight_layout()
plt.savefig('swarmplot_violin.png', dpi=300)
