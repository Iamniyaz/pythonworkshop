import pandas as pd
data = {'Name':['John','Alice','Bob','Emma','mike','sarah','aliyah'],
        'Age':[23,34,56,54,64,45,34],
        'city':['nyc','london','paris','hyd','la','berlin','tokye']}
df=pd.DataFrame(data)
print(df.head(3))
print(df.head())