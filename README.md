import pandas as pd
myData=pd.read_csv("F:\\Learning Resources Jan 2020\\liveProject\\Manning-Phishing-Websites-Detection-master\\Phishing.csv", header='infer')
myData.head(10)
myData.describe()
myData.columns

