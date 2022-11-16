import pandas as pd

data = pd.read_csv("BigmacPrice.csv")
c = 0
for i in data["local_price"]:
    c+=i
a = c/len(data)
print(a)
print(data.describe())