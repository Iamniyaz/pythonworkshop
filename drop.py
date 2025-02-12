import pandas as pd
data = {'Name':['John','Alice','Bob','Emma','mike','sarah','aliyah'],
        'Age':[23,34,56,54,64,45,34],
        'city':['nyc','london','paris','hyd','la','berlin','tokye']}
df=pd.DataFrame(data)
print(df.head(3))
print(df.head())
df.drop(4,axis=0,inplace=True)
df.drop([1,3],axis=0,inplace=True)
df.drop(index=5,inplace=True)

df.drop('Age',axis=1,inplace=True)
df.rename(columns={'Name':'First_Name'},inplace=True)
df.rename(mapper={'Age':'Number','City':'Address'},axis=1,inplace=True)
print(df)