import pandas as pd

# Load the cleaned dataset
df = pd.read_excel('Cleaned_Dataset.xlsx')

print("=" * 50)
print("STEP 1: BASIC STATISTICS")
print("=" * 50)

# Overall statistics
print("\n📊 General Statistics:")
print(df.describe())

# Average order value
print("\n💰 Average Order Value (TotalPrice):")
print("Mean:", round(df['TotalPrice'].mean(), 2))
print("Median:", round(df['TotalPrice'].median(), 2))
print("Min:", round(df['TotalPrice'].min(), 2))
print("Max:", round(df['TotalPrice'].max(), 2))

# Average quantity
print("\n📦 Average Quantity Ordered:")
print("Mean:", round(df['Quantity'].mean(), 2))
print("Median:", round(df['Quantity'].median(), 2))

print("\n" + "=" * 50)
print("STEP 2: TRENDS")
print("=" * 50)

print("\n🛍️ Top Selling Products:")
print(df['Product'].value_counts())

print("\n💳 Most Popular Payment Method:")
print(df['PaymentMethod'].value_counts())

print("\n📦 Order Status Breakdown:")
print(df['OrderStatus'].value_counts())

print("\n📱 Top Referral Sources:")
print(df['ReferralSource'].value_counts())

print("\n" + "=" * 50)
print("STEP 3: OUTLIER DETECTION")
print("=" * 50)

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower) | (df['TotalPrice'] > upper)]

print(f"\n📊 IQR Method Results:")
print(f"Lower Bound: {round(lower, 2)}")
print(f"Upper Bound: {round(upper, 2)}")
print(f"Total Outliers Found: {len(outliers)}")
print("\n🚨 Outlier Orders:")
print(outliers[['OrderID', 'Product', 'TotalPrice']].head(10))

print("\n" + "=" * 50)
print("STEP 4: CORRELATION ANALYSIS")
print("=" * 50)

correlation = df[['Quantity', 'UnitPrice', 
                   'ItemsInCart', 'TotalPrice']].corr()

print("\n📈 Correlation Matrix:")
print(correlation.round(2))

print("\n💡 Key Insight:")
print("Quantity vs TotalPrice correlation:", 
      round(df['Quantity'].corr(df['TotalPrice']), 2))
print("UnitPrice vs TotalPrice correlation:", 
      round(df['UnitPrice'].corr(df['TotalPrice']), 2))