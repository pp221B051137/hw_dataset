import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("BigmacPrice.csv")
dates = data["date"]

def for_date(year):
    cnt = 0
    for date in dates:
        if date[0:4] == year:
            cnt+=1
    return cnt
f2 = {0:['2000',for_date('2000')],1:['2001',for_date('2001')],2:['2002',for_date('2002')],3:['2003',for_date('2003')],4:['2004',for_date('2004')],5:['2005',for_date('2005')],6:['2006',for_date('2006')],7:['2007',for_date('2007')],8:['2008',for_date('2008')],9:['2009',for_date('2009')],10:['2010',for_date('2010')],11:['2011',for_date('2011')],12:['2012',for_date('2012')],13:['2013',for_date('2013')],14:['2014',for_date('2014')],15:['2015',for_date('2015')],16:['2016',for_date('2016')],17:['2017',for_date('2017')],18:['2018',for_date('2018')],19:['2019',for_date('2019')],20:['2020',for_date('2020')],21:['2021',for_date('2021')],22:['2022',for_date('2022')]}
Df = pandas.DataFrame(f2,index = ('Year','Number of countries'))

values = [for_date('2000'),for_date('2001'),for_date('2002'),for_date('2003'),for_date('2004'),for_date('2005'),for_date('2006'),for_date('2007'),for_date('2008'),for_date('2009'),for_date('2010'),for_date('2011'),for_date('2012'),for_date('2013'),for_date('2014'),for_date('2015'),for_date('2016'),for_date('2017'),for_date('2018'),for_date('2019'),for_date('2020'),for_date('2021'),for_date('2022')]
index = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
plt.bar(index,values,edgecolor='black')
print(Df)
plt.show()
