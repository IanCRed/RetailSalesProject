import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm

RetailSalesClean = pd.read_csv("RetailSalesClean.csv")

# SLR 

y = RetailSalesClean["Sales"]
x = RetailSalesClean["Customers"]
x = sm.add_constant(x)

SLRmodel = sm.OLS(y, x).fit()
print(SLRmodel.summary())

# MLR 

y = RetailSalesClean["Sales"]
x = RetailSalesClean[["Customers", "Promo", "CompetitionDistance", "SchoolHoliday", "StoreType", "Assortment", "CompetitionOpenSinceMonth"]]
x = sm.add_constant(x)

MLRmodel = smf.ols("Sales ~ Customers + Promo + CompetitionDistance + SchoolHoliday + C(StoreType) + C(Assortment) + CompetitionOpenSinceMonth", data=RetailSalesClean).fit()
print(MLRmodel.summary())

from statsmodels.stats.outliers_influence import variance_inflation_factor

X = MLRmodel.model.exog

vif = pd.DataFrame({
    "Variable": MLRmodel.model.exog_names,
    "VIF": [variance_inflation_factor(X, i) for i in range(X.shape[1])]
})

print(vif)

