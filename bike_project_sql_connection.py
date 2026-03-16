import pandas as pd
import pyodbc

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=DESKTOP-AQJSJK9\SQLEXPRESS;"
    r"DATABASE=bike_data;"
    r"Trusted_Connection=yes;"
    r"Encrypt=no;"
    r"TrustServerCertificate=yes;"
)

df = pd.read_sql_query("SELECT * FROM vw_bike_analysis", conn)



conn.close()

numeric_cols = ['riders','temp','atemp','hum','windspeed','revenue','profit']

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
print("Duplicates:", df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())
print(df[df['profit_margin'].isnull()].head())

# The dataset contains 1605 null values in profit_margin. 
#These correspond to records where no bikes were rented (riders = 0),
#resulting in zero revenue. Since profit margin is calculated as profit divided by revenue,
#the value is undefined in these cases. The missing values were kept for analytical accuracy.

df['profit_margin_clean'] = df['profit_margin'].fillna(0)

# ==============================
# 1. Descriptive Statistics Overview
# ==============================

print(df.describe())


#The dataset contains 34,758 records covering the period from 2021 to 2022.

#The average profit margin is approximately 68.8%, indicating a stable pricing structure.

#Profit margin remains nearly constant because it depends on fixed price and COGS.

#Temperature values are normalized between 0 and 1.

import matplotlib.pyplot as plt
# ==============================
# 2. Distribution of Riders
# ==============================

plt.hist(df['riders'], bins=30)
plt.title("Distribution of Riders")
plt.xlabel("Number of Riders")
plt.ylabel("Frequency")
plt.show()

# ==============================
# 3. Average Riders by Hour of the Day
# ==============================

df.groupby('hr')['riders'].mean().plot(kind='line')
plt.title("Average Riders by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Riders")
plt.show()

# ==============================
# 4. Average Riders by Day of the Week
# ==============================

df.groupby('weekday')['riders'].mean().plot(kind='bar')
plt.title("Average Riders by Weekday")
plt.xlabel("Day of Week")
plt.ylabel("Average Riders")
plt.show()

# ==============================
# 5. Bike Demand by Season
# ==============================

df.groupby('season')['riders'].mean().plot(kind='bar')
plt.title("Average Riders by Season")
plt.xlabel("Season")
plt.ylabel("Average Riders")
plt.show()


# ==============================
# 6. Bike Demand by Weather Conditions
# ==============================
df.groupby('weathersit')['riders'].mean().plot(kind='bar')
plt.title("Average Riders by Weather Situation")
plt.xlabel("Weather")
plt.ylabel("Average Riders")
plt.show()
# ==============================
# 7. Relationship Between Temperature and Riders
# ==============================

plt.scatter(df['temp'], df['riders'])
plt.title("Temperature vs Riders")
plt.xlabel("Temperature")
plt.ylabel("Riders")
plt.show()

# ==============================
# 8. Revenue Analysis by Season
# ==============================

df.groupby('season')['revenue'].sum().plot(kind='bar')
plt.title("Total Revenue by Season")
plt.xlabel("Season")
plt.ylabel("Revenue")
plt.show()

# ==============================
# 9. Profit Analysis by Season
# ==============================
df.groupby('season')['profit'].sum().plot(kind='bar')
plt.title("Total Profit by Season")
plt.xlabel("Season")
plt.ylabel("Profit")
plt.show()

# ==============================
# KEY INSIGHTS FROM EXPLORATORY DATA ANALYSIS
# ==============================

# 1. Bike rentals peak during typical commuting hours (around 8 AM and 5–6 PM),
#    indicating that many users rely on bikes for daily transportation.
#
# 2. Demand is highest during the summer season, suggesting that warmer weather
#    encourages more people to use bike-sharing services.
#
# 3. Weather conditions strongly affect bike usage, with lower demand observed
#    during poor weather situations.
#
# 4. Higher temperatures are positively associated with increased bike rental activity.
#
# 5. Revenue and profit follow the same seasonal trends as demand, with the highest
#    financial performance occurring during the summer months.