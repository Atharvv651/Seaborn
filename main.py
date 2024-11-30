import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Tips Dataset.csv')

print(df[['size', 'tip', 'total_bill']].describe())

sns.histplot(df['total_bill'], kde=True)
plt.show()

sns.scatterplot(data=df, x='total_bill', y='tip', hue='time')
plt.show()

sns.pairplot(df, hue='gender')
plt.show()
