## Vykreslení grafů - postup

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Následujicí řádek je potřeba pro zobrazení matplotlib grafů v Jupyter notebooku
%matplotlib inline 
```

0. Načíst data
    - Případně přejmenovat sloupce
    
	```python
	data = pd.read_csv(URL nebo soubor)
	```

1. Vytvořit obrázek

	```python
	plt.style.use('seaborn')
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
	ax.set_xlim()
	ax.set_ylim()
	ax.set_xlabel()
	ax.set_ylabel()
	ax.set_title()
	```