import pandas as pd 

RetailSalesClean = pd.read_csv("RetailSalesClean.csv")  
print(RetailSalesClean.head())

RetailSalesClean.info()
print(RetailSalesClean.describe())

print(RetailSalesClean["Sales"].describe())

print(RetailSalesClean.groupby("Year")["Sales"].mean())

print(RetailSalesClean.groupby(["Year"]).agg({"Sales" : "mean", "Customers" : "mean", "CompetitionDistance" : "mean"}))

# Creating a new column for Sales per Customer 

RetailSalesClean1 = RetailSalesClean.copy()
RetailSalesClean1["Sales_Per_Customer"] = RetailSalesClean["Sales"] / RetailSalesClean["Customers"]
print(RetailSalesClean1.head())

print(RetailSalesClean1.groupby(["Year"])["Sales"].mean().pct_change())

print(RetailSalesClean1.groupby(["Year"])["Customers"].mean().pct_change())

print(RetailSalesClean1.groupby(["Year"])["Sales_Per_Customer"].mean().pct_change()*100)

print(RetailSalesClean1.groupby(["Year"])["Sales"].sum())

import numpy as np 

print(RetailSalesClean1[["Sales", "Customers", "CompetitionDistance", "Sales_Per_Customer"]].corr())

RetailSalesClean2 = RetailSalesClean[["DayOfWeek", "Sales", "Customers", "Open", "Promo", "SchoolHoliday", "CompetitionDistance", "CompetitionOpenSinceMonth", "CompetitionOpenSinceYear", "Promo2", "Promo2SinceWeek", "Promo2SinceYear"]]

Retailcorr = RetailSalesClean2.corr().round(2)
print(Retailcorr.to_string())
Retailcorr.to_excel("RetailCorrelation.xlsx")

print(RetailSalesClean1.groupby(["StoreType"])["Sales"].mean())

print(RetailSalesClean1.pivot_table(index="Year", columns="StoreType", values="Sales"))
print(RetailSalesClean1.pivot_table(index="Year", columns="StoreType", values="Sales_Per_Customer"))
print(RetailSalesClean1.pivot_table(index="Year", values= "Sales"))