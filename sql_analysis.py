import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_excel('Cleaned_Dataset.xlsx')

# Create SQLite database
conn = sqlite3.connect('orders.db')
df.to_sql('orders', conn, if_exists='replace', index=False)

print("=" * 50)
print("✅ Database created successfully!")
print("✅ Table 'orders' loaded with", len(df), "rows")
print("=" * 50)

# Step 2 - Basic SELECT
print("\n📋 QUERY 1: First 5 Orders")
print("-" * 50)
query1 = "SELECT OrderID, Product, Quantity, TotalPrice FROM orders LIMIT 5"
result1 = pd.read_sql_query(query1, conn)
print(result1)

# Step 3 - WHERE filter
print("\n📋 QUERY 2: Delivered Orders Only")
print("-" * 50)
query2 = "SELECT OrderID, Product, TotalPrice FROM orders WHERE OrderStatus = 'Delivered' LIMIT 5"
result2 = pd.read_sql_query(query2, conn)
print(result2)

# Step 4 - ORDER BY
print("\n📋 QUERY 3: Top 5 Highest Value Orders")
print("-" * 50)
query3 = "SELECT OrderID, Product, TotalPrice FROM orders ORDER BY TotalPrice DESC LIMIT 5"
result3 = pd.read_sql_query(query3, conn)
print(result3)


# Step 5 - GROUP BY + COUNT
print("\n📋 QUERY 4: Orders Count by Product")
print("-" * 50)
query4 = """
SELECT Product, COUNT(*) as Total_Orders
FROM orders
GROUP BY Product
ORDER BY Total_Orders DESC
"""
result4 = pd.read_sql_query(query4, conn)
print(result4)

# Step 6 - GROUP BY + SUM
print("\n📋 QUERY 5: Total Revenue by Product")
print("-" * 50)
query5 = """
SELECT Product, ROUND(SUM(TotalPrice), 2) as Total_Revenue
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC
"""
result5 = pd.read_sql_query(query5, conn)
print(result5)

# Step 7 - GROUP BY + AVG
print("\n📋 QUERY 6: Average Order Value by PaymentMethod")
print("-" * 50)
query6 = """
SELECT PaymentMethod, ROUND(AVG(TotalPrice), 2) as Avg_Order_Value
FROM orders
GROUP BY PaymentMethod
ORDER BY Avg_Order_Value DESC
"""
result6 = pd.read_sql_query(query6, conn)
print(result6)

# Step 8 - WHERE + GROUP BY
print("\n📋 QUERY 7: Cancelled Orders by Product")
print("-" * 50)
query7 = """
SELECT Product, COUNT(*) as Cancelled_Orders
FROM orders
WHERE OrderStatus = 'Cancelled'
GROUP BY Product
ORDER BY Cancelled_Orders DESC
"""
result7 = pd.read_sql_query(query7, conn)
print(result7)

conn.close()
print("\n✅ All SQL Queries Executed Successfully!")