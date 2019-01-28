## Vykreslení grafů - postup

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Následujicí řádek je potřeba pro zobrazení matplotlib grafů v Jupyter notebooku
%matplotlib inline 

# Následujicí řádek udělá hezčí styl grafů
plt.style.use('seaborn')
```

0. Načíst data
    
	```python
	data = pd.read_csv(URL nebo soubor)
	```

1. Vytvořit obrázek

	```python
	fig, ax = plt.subplots(figsize=(10,6), dpi= 80)
	```

2. Přidat data

	```python
	plt.scatter(x, y, data)
	plt.bar(x, height, data)
	plt.hist(x)
	sns.boxplot(x, y, data)
	```

3. Přidat popisky

	```python
	ax.set(xlabel, ylabel, xlim, ylim, title)
	ax.set_xlim([0,10000])
	ax.set_ylim([0,10000])
	ax.set_xlabel('Váha těla, kg')
	ax.set_ylabel('Váha mozku, g')
	ax.set_title('Váha těla a mozku různých zvířat')
	```