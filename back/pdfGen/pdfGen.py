from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def createPDF(file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Title Box
    c.setStrokeColor(colors.purple)
    c.setLineWidth(1.5)
    c.rect(50, height - 58, 510, 30)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 50, f'Monthly Report:                                       {datetime.now().strftime("%B %Y")}')
    
    return c, width, height

def addIncomeData(c, width, height, income_data):
    # Income Statement
    c.setFont("Helvetica-Bold", 11)
    # c.rect(50, height - 200, 240, 70)
    c.drawString(60, height - 115, "INCOME STATEMENT")

    # Income Summary
    c.setFont("Helvetica-Bold", 10)
    c.drawString(60, height - 160, "Income:")
    c.rect(50, height - 180 - len(income_data) * 20, 240, len(income_data) * 20 )
    for i, data in enumerate(income_data):
        c.drawString(70, height - 200 - i * 20, f"{data['Category']}: {data['Amount']}")
    

def addExpensesData(c, width, height, expenses_data):
    # Expenses Summary
    c.setFont("Helvetica-Bold", 10)
    c.drawString(60, height-300, "Expenses:")
    c.rect(50, height - 315 - len(expenses_data) *20, 240, len(expenses_data) * 20)
    for i, data in enumerate(expenses_data):
        c.drawString(70, height - 335- i * 20, f"{data['Category']}: {data['Amount']}")



def addAssetsData(c, width, height, assets_data):
    # Balance Sheet
    c.setFont("Helvetica-Bold", 10)
    c.drawString(310, height - 115, "BALANCE SHEET")
    # c.rect(300, height - 320, 260, 160)

    # Assets Summary
    c.setFont("Helvetica-Bold", 10)
    c.drawString(310, height - 160, "Assets:")
    c.rect(300, height - 180 - len(assets_data) * 20, 260, len(assets_data) * 20)
    for i, data in enumerate(assets_data):
        c.drawString(320, height - 200 - i * 20, f"{data['Category']}: {data['Amount']}")


def addLiabilitiesData(c, width, height, liabilities_data):
    # Liabilities Summary
    c.setFont("Helvetica-Bold", 10)
    c.drawString(310, height - 280, "Liabilities:")
    c.rect(300, height - 300 - len(liabilities_data) * 20, 260, len(liabilities_data) * 20)
    for i, data in enumerate(liabilities_data):
        c.drawString(320, height - 315 - i * 20, f"{data['Category']}: {data['Amount']}")

def addFinancialStanding(c, width, height, total_income, total_expenses, total_assets, total_liabilities, net_savings, net_investment):
    # Financial Standing
    c.setFont("Helvetica-Bold", 14)
    c.rect(50, height - 530, 510, 100)
    c.drawString(60, height - 455, "FINANCIAL STANDING")
    c.setFont("Helvetica", 12)
    c.drawString(60, height - 480, f"Total income: {total_income}")
    c.drawString(200, height - 480, f"Total assets: {total_assets}")
    c.drawString(60, height - 500, f"Total expenses: {total_expenses}")
    c.drawString(200, height - 500, f"Total liabilities: {total_liabilities}")
    c.drawString(60, height - 520, f"Net savings: {net_savings}")
    c.drawString(200, height - 520, f"Net investment: {net_investment}")

def generateReport(file_name, income_data, expenses_data, assets_data, liabilities_data, total_income, total_expenses, total_assets, total_liabilities, net_savings, net_investment):
    c, width, height = createPDF(file_name)
    
    # Draw big rectangle enclosing everything
    c.rect(40, height - 800, 530, 780)
    
    # Add Income, Expenses, Assets, Liabilities, Financial Standing
    addIncomeData(c, width, height, income_data)
    addExpensesData(c, width, height, expenses_data)
    addAssetsData(c, width, height, assets_data)
    addLiabilitiesData(c, width, height, liabilities_data)
    addFinancialStanding(c, width, height, total_income, total_expenses, total_assets, total_liabilities, net_savings, net_investment)
    
    # Save the PDF
    c.save()

# Example data
income_data = [
    {"Category": "Work", "Amount": 5000},
    {"Category": "Stipend", "Amount": 10000},
    {"Category": "Family", "Amount": 20000},
    {"Category": "Dividends", "Amount": 5000},
    {"Category": "Work", "Amount": 7000},
    
    
]
expenses_data = [
    {"Category": "Rent", "Amount": 10000},
    {"Category": "Groceries", "Amount": 5000},
    {"Category": "Utilities", "Amount": 3000},
    {"Category": "Rent", "Amount": 10000},
  
    
]
assets_data = [
    {"Category": "Savings", "Amount": 50000},
    {"Category": "Stocks", "Amount": 20000},
    {"Category": "Property", "Amount": 100000},
    
]
liabilities_data = [
    {"Category": "Loan", "Amount": 30000},
    {"Category": "Credit Card", "Amount": 10000},
    {"Category": "Loan", "Amount": 30000},
    {"Category": "Credit Card", "Amount": 10000},
    {"Category": "Loan", "Amount": 30000},
    {"Category": "Credit Card", "Amount": 10000},
    
]

total_income = 47000
total_expenses = 18000
total_assets = 170000
total_liabilities = 40000
net_savings = 29000
net_investment = 70000

# Generate the report
generateReport(
    f'{datetime.now().strftime("%B %Y")}.pdf',
    income_data,
    expenses_data,
    assets_data,
    liabilities_data,
    total_income,
    total_expenses,
    total_assets,
    total_liabilities,
    net_savings,
    net_investment
)
