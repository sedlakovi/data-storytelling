## Seznámení s daty - postup

`import pandas as pd`

1. Načíst data
    - Případně přejmenovat sloupce
    
	`data = pd.read_csv(URL nebo soubor)`

2. V jakém formátu jsou sloupce?

	`data.dtypes`

3. Kolik je řádků a sloupců?

	`data.shape`

4. Obsahují některé sloupce chybějící data?

	`data.isnull().any()`

5. Udělat popisnou statistiku dat

	`data.describe(include='all')`
