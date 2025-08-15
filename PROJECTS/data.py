import numpy as np
import matplotlib.pyplot as plt 

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 100000],  # Paradise Biryani
    [2, 120000, 140000, 110000, 190000],  # Beijing Bites
    [3, 290000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 105000, 205000, 230000]   # Chai Point
])

print("==== zomato sales analysis ====")
print("\n SALES DATA SHAPE : ",sales_data.shape)
print("\n SALES DATA SHAPE FOR 3RD COMPANY :", sales_data[3])
print("\n SALES DATA FOR 1ST,2ND,3RD COMPANY :", sales_data[0:3])

#SALES
#SALES AS PER RESTAURANT
sales=np.sum(sales_data[:, 1:],axis=1)  #remove 1st column (restaurant_id) 
print("SALES PER RESTURENT FROM 2021 TO 2024 ", sales)

#SALES PER YEAR
sales_per_year = np.sum(sales_data[:, 1:], axis=0)  # sum across rows for each year
print("SALES PER YEAR FROM 2021 TO 2024 IN ZOMATO  ", sales_per_year)

#MINIMUM SALES PER RESTAURENT
min_sales = np.min(sales_data[:, 1:], axis=1)  # minimum sales for each restaurant
print("MINIMUM SALES PER RESTAURENT FROM 2021 TO 2024 ", min_sales)

#MAXIMUM SALES PER YEAR
max_sales = np.max(sales_data[:, 1:], axis=0)  
print("MAXIMUM SALES PER YEAR FROM 2021 TO 2024 ", max_sales)