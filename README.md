# Retail Sales Project
Sales Analytics via Python 

## Project Overview 
This project analyzes Rossmann retail store sales using Python to identify
key sales drivers, examine sales trends, and develop baseline forecasting
models

## Business Questions

- What factors are associated with higher sales?
- How do promotions affect sales?
- How do sales vary by store type and day of week?
- Can historical sales be used to forecast future sales?
- Which simple forecasting approach performs best?

## Tools

- Python
- Pandas
- NumPy
- Matplotlib / Plotly
- Statsmodels
- Scikit-learn

## Python Files
* [01_download_cleandata2.py](Code/01_download_cleandata2.py) : Load in and join Excel files
* [02_Exploratory_Analysis2.py](Code/02_Exploratory_Analysis2.py) : Data exploration
* [03_Regression_Analysis2.py](Code/03_Regression_Analysis2.py) : Regression
* [04_Advanced_Analytics2.py](Code/04_Advanced_Analytics2.py) : Rolling Averages and Forecasting
* [05_Visuals2.py](Code/05_Visuals2.py) : Data Visualizations
  
## Visuals

### Retail Sales Over Time 
[Retail Sales Over Time](https://iancred.github.io/RetailSalesProject/RetailSalesOverTime.html)

### Average Sales Per Year
![Avg_Sales.png](<Visuals/Avg_Sales.png>)

### Sales vs Customers Scatterplot
![Sales vs Customers](<Visuals/Sales v Customers.png>)

### Average Sales by Day
![Sales by Day](<Visuals/SalesbyDay.png>)

### Average Sales by Month
![Sales by Month](<Visuals/SalesbyMonth.png>)

## Regression Results 
### Baseline MLR 
![Multiple Linear Regression](<Visuals/Retail MLR Results1.png>)

### MLR with rolling averages
![MLR Rolling Averages](<Visuals/OLS with rolling avg.png>)

## Forecasting and Rolling Averages 
[Rolling Average vs Actual Sales](https://iancred.github.io/RetailSalesProject/DailySalesRolling7.html)

then forecast with regression vs sales 

## Key Takeaways 
* The strongest predictors of retail sales were customer traffic and promotions. 
* Simple forecasting methods have limitations : 7-Day rolling averages produced an MAE of 2,332.14. Which means predictions differed from actual daily sales by $2,332.14. Mean average sales were $5,398.98.
* Forecasting based on regression was more accurate : When forecasting based off of our MLR, the MAE produced was 831.15, a significant improvement from 2,332.14.  
