import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv('BigmacPrice.csv')
d = d.drop_duplicates(subset=["name"])

print("Number of countries: ",len(d))
print(d['currency_code'].to_list())
