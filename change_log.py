from fpdf import FPDF
import datetime

pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font('Helvetica', 'B', 20)
pdf.cell(0, 15, 'Data Cleaning Change Log', ln=True, align='C')
pdf.set_font('Helvetica', '', 11)
pdf.cell(0, 10, 'Project 1 - DecodeLabs Internship | Batch 2026', ln=True, align='C')
pdf.cell(0, 10, f'Date: {datetime.date.today()}', ln=True, align='C')
pdf.ln(10)

# Table Header
pdf.set_font('Helvetica', 'B', 11)
pdf.set_fill_color(30, 30, 100)
pdf.set_text_color(255, 255, 255)
pdf.cell(25, 10, 'Change ID', border=1, fill=True)
pdf.cell(65, 10, 'Description', border=1, fill=True)
pdf.cell(60, 10, 'Impact', border=1, fill=True)
pdf.cell(30, 10, 'Status', border=1, ln=True, fill=True)

# Table Rows
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(0, 0, 0)

# Row 1
pdf.set_fill_color(240, 240, 240)
pdf.cell(25, 10, 'CR001', border=1, fill=True)
pdf.cell(65, 10, 'Filled missing CouponCode with NO_COUPON', border=1, fill=True)
pdf.cell(60, 10, 'Fixed 309 missing values', border=1, fill=True)
pdf.cell(30, 10, 'Resolved', border=1, ln=True, fill=True)

# Row 2
pdf.set_fill_color(255, 255, 255)
pdf.cell(25, 10, 'CR002', border=1, fill=True)
pdf.cell(65, 10, 'Rounded UnitPrice to 2 decimals', border=1, fill=True)
pdf.cell(60, 10, 'Consistent price formatting', border=1, fill=True)
pdf.cell(30, 10, 'Resolved', border=1, ln=True, fill=True)

# Row 3
pdf.set_fill_color(240, 240, 240)
pdf.cell(25, 10, 'CR003', border=1, fill=True)
pdf.cell(65, 10, 'Rounded TotalPrice to 2 decimals', border=1, fill=True)
pdf.cell(60, 10, 'Consistent price formatting', border=1, fill=True)
pdf.cell(30, 10, 'Resolved', border=1, ln=True, fill=True)

pdf.ln(10)

# Summary
pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 10, 'Summary:', ln=True)
pdf.set_font('Helvetica', '', 10)
pdf.cell(0, 8, 'Total Issues Found: 3', ln=True)
pdf.cell(0, 8, 'Total Issues Resolved: 3', ln=True)
pdf.cell(0, 8, 'Dataset Rows: 1200 | Columns: 14', ln=True)
pdf.cell(0, 8, 'Final Status: CLEAN - Ready for Analysis', ln=True)

pdf.output('Change_Log.pdf')
print("Change Log PDF created successfully!")