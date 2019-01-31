## Seznámení s daty - postup

`import pandas as pd`

1. Načíst data

    ```python
    data = pd.read_csv(URL nebo soubor)
    ```
     - Případně přejmenovat sloupce

         ```python
         data.rename(index=str,
                     columns={
                        'Unnamed: 0': 'Sloupec1'
                     },
                     inplace=True)
         ```

2. V jakém formátu jsou sloupce?

    ```python
    data.dtypes
    ```

3. Kolik je řádků a sloupců?

    ```python
    data.shape
    ```

4. Obsahují některé sloupce chybějící data?

    ```python
    data.isnull().any()
    ```

5. Udělat popisnou statistiku dat

    ```python
    data.describe(include='all')
    ```
