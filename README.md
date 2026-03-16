## 🚲 Bike Sharing Demand Analysis
# 📌 Project Overview

Bike-sharing systems play an increasingly important role in urban transportation. Understanding when and why people rent bikes can help operators optimize bike availability, improve service efficiency, and maximize revenue.

The goal of this project is to analyze historical bike-sharing data and identify key patterns influencing bike rental demand.

# 📊 Dataset Description

The dataset contains historical bike rental data with information about:

Date and time of rentals

Weather conditions

Temperature

Seasonality

Number of riders

Revenue and profit metrics

The data was stored in Microsoft SQL Server and accessed using Python with pandas.

# ⚙️ Data Preparation

Data preparation included:

Connecting to the SQL Server database

Creating a SQL view combining multiple tables

Checking for duplicates and missing values

Investigating null values in the profit_margin column

Null values in profit_margin occur when no bikes were rented (riders = 0), resulting in zero revenue. Since profit margin is calculated as profit divided by revenue, the value becomes undefined in those cases.

# 🔎 Exploratory Data Analysis (EDA)

The analysis explored several aspects of bike demand:

Distribution of riders

Demand by hour of the day

Demand by weekday

Demand by season

Impact of weather conditions

Relationship between temperature and rider count

Revenue and profit patterns across seasons

Visualizations were created using Matplotlib.

# 📈 Key Insights

1️⃣ Bike demand peaks during commuting hours, particularly around 8 AM and 5–6 PM.

2️⃣ Demand for bike rentals is highest during the summer season.

3️⃣ Weather conditions significantly influence bike usage.

4️⃣ Higher temperatures are associated with increased bike rental activity.

5️⃣ Revenue and profit follow the same seasonal patterns as bike demand.

# 💡 Business Recommendations

Based on the analysis, several recommendations can be made:

Increase bike availability during peak commuting hours.

Allocate more bikes during warmer seasons when demand is highest.

Introduce promotions during winter months to stimulate demand.

Use weather forecasts to anticipate demand changes and adjust bike distribution accordingly.

# 🛠 Tools & Technologies

Python

Pandas

Matplotlib

SQL

Microsoft SQL Server

Visual Studio Code

# 📌 Conclusion

The analysis demonstrates that bike-sharing demand is strongly influenced by time of day, seasonal patterns, and weather conditions.

Understanding these patterns can help bike-sharing operators improve operational efficiency, optimize resource allocation, and increase profitability.
