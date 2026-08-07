import pandas as pd 

RSC = pd.read_csv("RetailSalesClean.csv")

RSC["Date"] = pd.to_datetime(RSC["Date"])

RSC = RSC.sort_values(["Store", "Date"])

#Yesterdays sales
RSC["Lag1"] = (RSC.groupby("Store")["Sales"].shift(1))
print(RSC.head(10))

#Last week sales
RSC["Lag7"] = (RSC.groupby("Store")["Sales"].shift(7))
print(RSC.head(10))

#Rolling averages 
RSC["Rolling7"] = (RSC.groupby("Store")["Sales"].transform(lambda x: x.shift(1).rolling(7).mean()))
print(RSC.head(10))

store54 = RSC[RSC["Store"] == 54]
print(store54.head(10))

import matplotlib.pyplot as plt

plt.plot(store54["Date"], store54["Sales"], label="Sales")
plt.show()

plt.plot(store54["Date"], store54["Rolling7"], label="7 Day Average")
plt.show()

# Forecast with store 54
store54 = store54.set_index("Date")
store54["Forecast"] = (store54["Sales"].rolling(7).mean().shift(1))
plt.plot(store54.index, store54["Sales"], label="Actual")
plt.plot(store54.index, store54["Forecast"], label="Forecast")
plt.show()

#Create Forecast column 

RSC["Forecast"] = (RSC.groupby("Store")["Sales"].transform(lambda x: x.shift(1).rolling(7).mean()))

# MAE (difference between forecasted and actual) 

from sklearn.metrics import mean_absolute_error, mean_squared_error

valid = RSC.dropna(subset=["Forecast"])
mae = mean_absolute_error(valid["Sales"], valid["Forecast"])
print(mae)

print(RSC["Sales"].describe())

# Rolling average forecast predicts future sales based on historical sales 
# Regression (explanatory models) explains what drives sales and estimates relationships 

# Creating new regression model with lag variables included 
import statsmodels.formula.api as smf
import statsmodels.api as sm

model = smf.ols("Sales ~ Customers + Promo + CompetitionDistance + SchoolHoliday + C(StoreType) + C(Assortment) + CompetitionOpenSinceMonth + Lag1 + Lag7", data=RSC).fit()
print(model.summary())

RSC["Forecast2"] = model.predict(RSC)
print(RSC.head(10))

valid2 = RSC.dropna(subset=["Forecast2"])
mae2 = mean_absolute_error(valid2["Sales"], valid2["Forecast2"])
print(mae2)

# MAE2 = 831.15 a significant improvement over the rolling average forecast MAE = 2,332.1
# MAE2 used the regression model to forecast sales while MAE1 used the rolling average forecast. 
