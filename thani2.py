import pandas as pd
data=pd.read_csv("C://Users/tanne/OneDrive/Desktop/matches.csv")
#print(data)
#print(data.head())
#print(data.tail())
#print(data.head(10))
#print(data.tail(15))
#print(data[100:110])
#print(data[200:237])
#print(data[:57])
#print(data[437:])

#print(data.columns)
#print(data[data['Season']==2008].shape[0])
#print(data[data['Season']==2009])
#print(data[data['Winner']=='Kolkata Knight Riders'])

print(data[data['City']=="banglore"])