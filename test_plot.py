import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('test_installation.csv')
sns.set()
plt.scatter(x='x', y='y', data=data, alpha=0.7)
plt.show(block=True)
# Jestli vidite kodové slovo v grafu, nainstalovali jste vsechno uspešně :)