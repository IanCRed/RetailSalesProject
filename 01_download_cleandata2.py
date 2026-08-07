import pandas as pd 

Train = pd.read_csv("train.csv")
print(Train.head())

Store = pd.read_csv("store.csv")
print(Store.head())

RetailSales = Train.merge(Store, how="left", on="Store")
print(RetailSales.head(10))

print(RetailSales.info())

RetailSales.isnull().sum() 

RetailSalesClean = RetailSales.dropna()
RetailSalesClean["Date"] = pd.to_datetime(RetailSalesClean["Date"])
print(RetailSalesClean.info())

RetailSalesClean["Year"] = RetailSalesClean["Date"].dt.year
RetailSalesClean["Month"] = RetailSalesClean["Date"].dt.month
print(RetailSalesClean.head())

#Check for Duplicates 
print(RetailSalesClean.duplicated().sum())

#There are none. but if there were, we could remove them with the following line of code:

RetailSalesClean = RetailSalesClean.drop_duplicates()

print((RetailSalesClean["Sales"] < 0).sum())

print((RetailSalesClean["Customers"] == 0).sum())

print(((RetailSalesClean["Sales"] > 0) & (RetailSalesClean["Customers"] <= 0)).sum())

print(RetailSalesClean.describe())

RetailSalesClean.dropna(inplace=True)

RetailSalesClean.to_csv("RetailSalesClean.csv", index=False)