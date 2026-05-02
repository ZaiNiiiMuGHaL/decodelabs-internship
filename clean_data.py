import pandas as pd

# Load the dataset
df = pd.read_excel('Dataset for Data Analytics.xlsx')

# See the first 5 rows
print(df.head())

# See shape (rows, columns)
print("Shape:", df.shape)

# See missing values
print(df.isnull().sum())

df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
print ('Missing Values after fix:')
print(df.isnull().sum())

df["UnitPrice"] =df["UnitPrice"].round(2)
df["TotalPrice"]=df["TotalPrice"].round(2)

print("Sample Prices after fix:")
print(df[["UnitPrice", "TotalPrice"]].head(5))

df.to_excel("Cleaned_Dataset.xlsx", index=False)
print("Cleaned Dataset saved successfully!")