import pandas
empty = []
data = pandas.read_csv("BigmacPrice.csv")
data = data.drop_duplicates(subset=["name"])
data = data[['name','currency_code','local_price']]

id = str(input())
name = data.loc[data['currency_code']==id]['name']#,'local_price'
price = data.loc[data['currency_code']==id]['local_price']
if list(name) == empty:
    print("[",id,"]","does not exist")
else:
    print("[",id,"]")
    print("country:",name.to_string().split()[1:])
    print("price: ",price.to_string().split()[1])