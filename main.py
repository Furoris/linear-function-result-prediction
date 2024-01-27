import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#Get and validate input
price = 0
while price < 1000 or price > 10000:
    price = input("Please enter square feet area of home (1000-10000): ")
    try:
        price = int(price)
    except ValueError:
        price = 0

#Read data frame
df = pd.read_csv("homeprices.csv")

#Visualization part
plt.xlabel('Area (sqr ft)')
plt.ylabel('Price (USD)')
plt.scatter(df.area, df.price, color='blue', marker='+')
#plt.show()

#Fitting linear model
reg = linear_model.LinearRegression()
reg.fit(df[['area']].values, df.price)

#Prediction of price
prediction = reg.predict([[price]])
print("Predicted price $" + str(round(prediction[0], 2)))
