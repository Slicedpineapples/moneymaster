from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def reportSummary(file_name):
    reportMothYear = datetime.now().strftime("%B %Y")

    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4 

    c.rect(50, height - 58, 510, 30)
    c.setStrokeColor(colors.purple)
    c.setLineWidth(1.5)
    
    # Setting the title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, height - 50, f'Monthly Report: {reportMothYear}')
    
    c.rect(50, height - 125, 510, 30)
    c.setStrokeColor(colors.purple)
    c.setLineWidth(1.5)
    

    # Income Statement and Balance Sheet
    c.rect(50, height - 400, 240, 260)  # Income Statement Box
    c.rect(300, height - 400, 260, 260)  # Balance Sheet Box
    
    # Income Statement
    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, height - 115, "INCOME STATEMENT")
    c.setFont("Helvetica", 10)


    # INCOME SUMMARY
    c.setFont("Helvetica-Bold", 10)
    c.drawString(60, height - 160, "Income:")
    for i in range(3):
        c.drawString(70, height - 180 - i*20, f"{i+1}.")

    # EXPENSES SUMMARY
    c.setFont("Helvetica-Bold", 10)
    c.drawString(60, height - 250, "Expenses:")
    for i in range(3):
        c.drawString(70, height - 270 - i*20, f"{i+1}.")
    
    # Balance Sheet
    c.setFont("Helvetica-Bold", 12)
    c.drawString(310, height - 115, "BALANCE SHEET")
    
    # ASSETS SUMMARY
    c.setFont("Helvetica-Bold", 10)
    c.drawString(310, height - 160, "Assets:")
    for i in range(5):
        c.drawString(320, height - 180 - i*20, f"{i+1}.")
    
    # LIABILITIES SUMMARY
    c.setFont("Helvetica-Bold", 10)
    c.drawString(310, height - 280, "Liabilities:")
    for i in range(5):
        c.drawString(320, height - 300 - i*20, f"{i+1}.")
    
    # Financial Standing
    c.setFont("Helvetica-Bold", 14)
    c.rect(50, height - 465, 510, 30)
    c.drawString(60, height - 455, "FINANCIAL STANDING")
    
    c.setFont("Helvetica", 12)
    c.drawString(60, height - 500, "Total income: ______")
    c.drawString(200, height - 500, "Total assets: ______")
    c.drawString(60, height - 520, "Total expenses: ______")
    c.drawString(200, height - 520, "Total liabilities: ______")
    c.drawString(60, height - 540, "Net savings: ______")
    c.drawString(200, height - 540, "Net investment: ______")

    # Save the PDF
    c.save()

# Generate the report
reportSummary("Monthly_Report_May_2024.pdf")
