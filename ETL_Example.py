# It is the easiest way, if you try out each step in Jupyter Lab.

import pandas as pd
import sqlite3

# Step 1: Extract
# Reading data from the csv file
file_path = "C:/Users/schue/Downloads/customer_data_book_purchase_fictional_bookstore.csv" 
data = pd.read_csv(file_path)
print("Extracted data:")
print(data.head())


# Step 2: Transform
# Creating a new column Full_Name by combining First_Name and Last_Name
data['Full Name'] = data['First Name'] + ' ' + data['Last Name']

# Create a new column High_Payment with "Yes" if Paid_Price > 20, otherwise "No"
data['High_Payment'] = data['Price_Paid'].apply(lambda x: 'Yes' if x > 20 else 'No')


print("Transformed data:")
print(data.head())


# Step 3: Load 
# Connecting to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('output_database.db')

# Loading the DataFrame into a new table in the SQLite database
data.to_sql('transformed_data', conn, if_exists='replace', index=False)

# Analysis: Identifying how many customers made high payments
high_payment_count = data[data['High_Payment'] == 'Yes'].count()
print("Number of High Payments:", high_payment_count['High_Payment'])

# Close the database connection
conn.close()

print("ETL process completed. Transformed data saved to 'output_database.db'.")


import matplotlib.pyplot as plt

# Visualizing the data - Example: Distribution of prices paid
data['Price_Paid'].hist(bins=10)
plt.title('Distribution of Prices Paid')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()



