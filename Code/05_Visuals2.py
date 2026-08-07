import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from plotly import express as px

RSC = pd.read_csv("RetailSalesClean.csv")
RSC["Date"] = pd.to_datetime(RSC["Date"])
print(RSC.info())

# Retail Sales Over Time interactive plot using Plotly
fig1 = px.line(RSC, x="Date", y="Sales", title="Retail Sales Over Time")
fig1.show()
fig1.write_html("RetailSalesOverTime.html")


#Bar Chart of Average Sales by Store Type
avgsalesperstore = RSC.groupby("StoreType")["Sales"].mean() 

x = avgsalesperstore.index
y = avgsalesperstore.values
plt.bar(x, y, color = "green", edgecolor = "black")
plt.xlabel("Store Type")
plt.ylabel("Average Sales")
plt.title("Average Sales by Store Type")
bars = plt.bar(x, y, color = "green", edgecolor = "black")
plt.bar_label(bars, fmt='$%.0f')
plt.show()

# Scatterplot of Sales vs Customers
RSC.sample
plt.scatter(RSC["Customers"], RSC["Sales"], color = "blue", edgecolor="black", alpha=0.7)
plt.title("Sales vs Customers")
plt.xlabel("Number of Customers")   
plt.ylabel("Sales") 
plt.show()

# Line Chart of Average Sales by Day of the Week
avgsalesbyday = RSC.groupby("DayOfWeek")["Sales"].mean()
x = avgsalesbyday.index
y = avgsalesbyday.values
plt.bar(x, y, color = "orange", edgecolor = "black")
plt.xlabel("Day of the Week")
plt.ylabel("Average Sales")
plt.title("Average Sales by Day of the Week")   
bars = plt.bar(x, y, color = "orange", edgecolor = "black")
plt.bar_label(bars, fmt='$%.0f')
plt.show()

monthlyavg = RSC.groupby("Month")["Sales"].mean()
x = monthlyavg.index
y = monthlyavg.values
plt.bar(x, y, color = "purple", edgecolor = "black")
plt.xlabel("Month: Jan-Dec")
plt.ylabel("Average Sales")
plt.title("Average Sales by Month")
plt.show()

# creating rolling average 
RSC.info()
daily_sales = (RSC.groupby("Date")["Sales"].sum().sort_values("Date"))
daily_sales["Rolling7"] = daily_sales["Sales"].rolling(7).mean()
daily_sales["Forecast"] = daily_sales["Sales"].rolling(7).mean().shift(1)

fig3 = px.line(daily_sales, x="Date", y=["Sales", "Rolling7"], title = "Company-Wide Daily Sales vs 7-Day Rolling Average")
fig3.show()


