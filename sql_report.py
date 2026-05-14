from fpdf import FPDF
import datetime

pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font('Helvetica', 'B', 20)
pdf.cell(0, 15, 'SQL Data Analysis Report', ln=True, align='C')
pdf.set_font('Helvetica', '', 11)
pdf.cell(0, 10, 'Project 3 - DecodeLabs Internship | Batch 2026', ln=True, align='C')
pdf.cell(0, 10, f'Date: {datetime.date.today()}', ln=True, align='C')
pdf.ln(5)

# Query 1
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 1: Basic SELECT', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Retrieved first 5 orders with OrderID, Product, Quantity and TotalPrice.', ln=True)
pdf.ln(3)

# Query 2
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 2: WHERE Filter - Delivered Orders', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Filtered only Delivered orders using WHERE OrderStatus = Delivered.', ln=True)
pdf.cell(0, 8, 'Insight: Only 231 out of 1200 orders were successfully delivered.', ln=True)
pdf.ln(3)

# Query 3
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 3: ORDER BY - Top 5 Highest Orders', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Sorted orders by TotalPrice DESC to find highest value orders.', ln=True)
pdf.cell(0, 8, 'Highest: ORD200789 - Tablet - Rs.3456.40', ln=True)
pdf.ln(3)

# Query 4
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 4: GROUP BY + COUNT - Orders by Product', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Printer: 181 orders (MOST POPULAR)', ln=True)
pdf.cell(0, 8, 'Phone: 156 orders (LEAST POPULAR)', ln=True)
pdf.ln(3)

# Query 5
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 5: GROUP BY + SUM - Revenue by Product', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Chair: Rs.195,620.11 (HIGHEST REVENUE) - Surprise winner!', ln=True)
pdf.cell(0, 8, 'Phone: Rs.151,722.39 (LOWEST REVENUE)', ln=True)
pdf.cell(0, 8, 'Insight: Most orders does not mean most revenue!', ln=True)
pdf.ln(3)

# Query 6
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 6: AVG - Order Value by Payment Method', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Credit Card: Rs.1127.55 avg (HIGHEST SPENDERS)', ln=True)
pdf.cell(0, 8, 'Debit Card: Rs.1001.56 avg (LOWEST SPENDERS)', ln=True)
pdf.ln(3)

# Query 7
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  QUERY 7: WHERE + GROUP BY - Cancelled Orders', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, 'Chair: 45 cancellations (MOST CANCELLED!)', ln=True)
pdf.cell(0, 8, 'Phone: 31 cancellations (LEAST CANCELLED)', ln=True)
pdf.cell(0, 8, 'Insight: Chair earns most BUT also gets cancelled most!', ln=True)
pdf.ln(5)

# Recommendations
pdf.set_font('Helvetica', 'B', 13)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '  FINAL BUSINESS RECOMMENDATIONS', ln=True, fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 10)
pdf.ln(3)
pdf.cell(0, 8, '1. Investigate Chair cancellations - highest revenue at risk!', ln=True)
pdf.cell(0, 8, '2. Promote Phone category - lowest orders and revenue!', ln=True)
pdf.cell(0, 8, '3. Encourage Credit Card payments - highest avg order value!', ln=True)
pdf.cell(0, 8, '4. Focus on delivery success rate - only 231/1200 delivered!', ln=True)

pdf.output('SQL_Report.pdf')
print("SQL Report PDF created successfully!")