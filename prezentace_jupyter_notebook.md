## Vytvoření slidů pomocí Jupyter Notebooku

1. Vytvořte Jupiter notebook
2. Přejděte do slideshow mode
	View -> Cell Toolbar -> Slideshow
	
3. U každé buňky si můžete vybrat jak se zobrazí v prezentaci

- Slide
- Subslide
- Fragment
- Skip

4. Spusťte slidy

V terminálu použijte následující příkaz:

`jupyter nbconvert *.ipynb --to slides --post serve`

Slidy se otevřou v prohlížeči.

Pro více informací se podívejte na tutoriál [zde](https://medium.com/learning-machine-learning/present-your-data-science-projects-with-jupyter-slides-75f20735eb0f)