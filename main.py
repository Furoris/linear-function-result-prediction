import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Get and validate input
area = 0
while area < 1000 or area > 10000:
    area = input("Please enter square feet area of home (1000-10000): ")
    try:
        area = int(area)
    except ValueError:
        area = 0

# Read data frame
df = pd.read_csv("homeprices.csv")

# Visualization part
plt.xlabel('Area (sqr ft)')
plt.ylabel('Price (USD)')
plt.scatter(df.area, df.price, color='blue', marker='+')
# plt.show()

# Fitting linear model
reg = linear_model.LinearRegression()
reg.fit(df[['area']].values, df.price)

# Prediction of price
prediction = reg.predict([[area]])
print("Predicted price $" + str(round(prediction[0], 2)))
