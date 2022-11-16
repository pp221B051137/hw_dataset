import pandas as pd
data = pd.read_csv("BigmacPrice.csv")

prices = data["local_price"]

all_price = []

max = prices.describe()[len(prices.describe())-1]
min = prices.describe()[3]
ev = (data.index[data['local_price']==max].tolist())
ev2 = (data.index[data['local_price']==min].tolist())
name1 = data.loc[ev,"name"]
name2 = data.loc[ev2,"name"]

for i in name1:
    for j in name2:
        f = {'max':[ev,i,max],'min':[ev2,j,min]}
        df = pd.DataFrame(f,index=('id','country','price'))
        print(df)