# 🧪 DecodeLabs Internship — Data Analytics
**Intern:** Muhammad Zain Shoukat
**Batch:** 2026
**Company:** DecodeLabs, Greater Lucknow, India

---

## 📁 Project 1 — Data Cleaning & Preparation

### 🎯 Goal
Clean a raw dataset by handling missing values, duplicates, and incorrect data formats.

### 🛠 Tools Used
- Python 3
- Pandas Library
- FPDF2 Library

### 🔍 Issues Found & Fixed

| Change ID | Issue | Fix Applied | Status |
|---|---|---|---|
| CR001 | 309 missing CouponCode values | Filled with NO_COUPON | ✅ Resolved |
| CR002 | UnitPrice inconsistent decimals | Rounded to 2 decimal places | ✅ Resolved |
| CR003 | TotalPrice inconsistent decimals | Rounded to 2 decimal places | ✅ Resolved |

### 📦 Files
- `clean_data.py` — Python script for data cleaning
- `Cleaned_Dataset.xlsx` — Final cleaned dataset
- `Change_Log.pdf` — Professional documentation of all changes

### 📊 Dataset Info
- Total Rows: 1200
- Total Columns: 14
- Final Status: ✅ CLEAN — Ready for Analysis


---

## 📁 Project 2 — Exploratory Data Analysis (EDA)

### 🎯 Goal
Analyze the cleaned dataset to uncover patterns, trends and outliers.

### 🛠 Tools Used
- Python 3
- Pandas Library
- FPDF2 Library

### 🔍 Key Findings
- Average order value: 1053.97 (Right Skewed Data)
- Top selling product: Printer (181 orders)
- 41% orders cancelled/returned — major business risk!
- Instagram is #1 traffic source
- 8 high-value outlier orders detected
- UnitPrice is strongest revenue driver (0.72 correlation)

### 📦 Files
- `eda.py` — EDA Python script
- `EDA_Report.pdf` — Business insights report