import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('medical_examination_small.csv')

#df["BMI"] = df["weight"] / (df["height"]/100)**2
df["overweight"] = (df["weight"] / (df["height"]/100)**2).apply(lambda x: 1 if x > 25 else 0)

# Map cholesterol and gluc values to 0 or 1
df['cholesterol'] = df['cholesterol'].map(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].map(lambda x: 0 if x == 1 else 1)

# Set the style for the plots
sns.set(style='whitegrid')

# Create the catplot for cardio
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'smoke'])
df_cat_plot = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=6, aspect=1)
#g1 = sns.catplot(x='variable', hue='value', col='cardio', data=pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'smoke']), kind='count', height=6, aspect=1)
df_cat_plot.set_axis_labels("variable", "total")

# Show the plot
plt.show()
fig = df_cat_plot

# Do not modify the next two lines
fig.savefig('catplot.png')
# Save plot to the file
df_cat_plot.savefig('Figure1.png')


# Clean the data.
# Filter out the following patient segments that represent incorrect data:
# If diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi'])) and in another way remove last 0 from ap_lo value
df.loc[df['ap_lo'] > df['ap_hi'], 'ap_lo'] = df.loc[df['ap_lo'] > df['ap_hi'], 'ap_lo'].astype(str).str[:-1]

# height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
df.loc[df['height'] <= df['height'].quantile(0.025), 'height'] = df['height'].quantile(0.025)

# height is more than the 97.5th percentile
df.loc[df['height'] > df['height'].quantile(0.975), 'height'] = df['height'].quantile(0.975)

# weight is less than the 2.5th percentile
df.loc[df['weight'] <= df['weight'].quantile(0.025), 'weight'] = df['weight'].quantile(0.025)

# weight is more than the 97.5th percentile
df.loc[df['weight'] > df['weight'].quantile(0.975), 'weight'] = df['weight'].quantile(0.975)

print(df)

# calculate the correlation matrix
corr_matrix = df.corr()

# create a mask to hide the upper triangle of the heatmap
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# plot the heatmap
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm')

# show the plot
plt.show()