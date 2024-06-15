from collections import defaultdict
from server import connect

#Making a select querry for income. It will fetch all incomes, then categorice them by category and sum them up.The result will be a list of dictionaries.
def incomeRawData(userId, start, end):
    income = connect()
    cursor = income.cursor()

    cursor.execute("SELECT sourceAmountId, incomeCategoryId FROM income WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_data = []

    for row in result1:
        sourceAmountId = row[0]
        incomeCategoryId = row[1]

        cursor.execute("SELECT amount FROM incomeSource WHERE id = %s", (sourceAmountId,)) #commented out sourceName
        result2 = cursor.fetchall()
        # sourceName = result2[0][0]
        amount = result2[0][0]

        cursor.execute("SELECT incomeName FROM incomeCategory WHERE id = %s", (incomeCategoryId,))
        result3 = cursor.fetchall()
        incomeName = result3[0][0]

        report_data.append({ 
            # "sourceName": sourceName,
            "amount": amount,
            "incomeName": incomeName,
        })
    total_income = sum([data['amount'] for data in report_data])
    total_income = ({total_income}) #parsing it a s float
    total_income = total_income.pop() #parsing it as a float

    return  report_data, total_income

# print(incomeRawData(2, '2024-05-01', '2024-5-31')[1]) #testing the function

#Making a select querry for expenses. It will fetch all expenses, then categorice them by category and sum them up.The result will be a list of dictionaries.

from collections import defaultdict

def expensesRawData(userId, start, end):
    expenses = connect()
    cursor = expenses.cursor()

    cursor.execute("SELECT expenseCategoryId, expensesPriceId FROM expenses WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    expense_groups = defaultdict(int)

    for row in result1:
        expenseCategoryId = row[0]
        expensesPriceId = row[1]

        cursor.execute("SELECT expenseName FROM expensesCategory WHERE id = %s", (expenseCategoryId,))
        result2 = cursor.fetchone()  # Since we are fetching a single value, use fetchone()

        if result2:
            expenseName = result2[0]

            cursor.execute("SELECT Price FROM expensesPrice WHERE id = %s", (expensesPriceId,))
            result3 = cursor.fetchone()

            if result3:
                price = result3[0]
                expense_groups[expenseName] += price

    # Convert grouped dictionary to final report format
    report_data = []
    total_expenses = 0
    for expenseName, total_price in expense_groups.items():
        report_data.append({
            "expenseName": expenseName,
            "total_price": total_price,
        })
        total_expenses += total_price

    cursor.close()
    return report_data, total_expenses


# print(expensesRawData(2, '2024-05-01', '2024-6-30')[1]) #testing the function

#Making a select querry for assets. It will fetch all assets, then categorice them by category and sum them up.The result will be a list of dictionaries.
def assetsRawData(userId, start, end):
    assets = connect()
    cursor = assets.cursor()

    cursor.execute("SELECT assetCategoryId, value FROM assets WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_data = []
    for row in result1:
        assetCategoryId = row[0]
        value = row[1]

        cursor.execute("SELECT assetName, numberOfItems, location FROM assetsCategory WHERE id = %s", (assetCategoryId,))
        result2 = cursor.fetchall()
        assetName = result2[0][0]
        numberOfItems = result2[0][1]
        location = result2[0][2]

        report_data.append({
            "location": location,
            "assetName": assetName,
            "value": value,
            "numberOfItems": numberOfItems,
        })
    total_assets = sum([data['value'] for data in report_data])
    total_assets = ({total_assets})
    total_assets = total_assets.pop()   #parsing it as a float

    cursor.close()
    return report_data, total_assets
# print(assetsRawData(2, '2024-05-01', '2024-5-31')) #testing the function

#Making a select querry for liabilities. It will fetch all liabilities, then categorice them by category and sum them up.The result will be a list of dictionaries.
def liabilitiesRawData(userId, start, end):
    liabilities = connect()
    cursor = liabilities.cursor()

    cursor.execute("SELECT liabilityCategoryId, dateDue FROM liabilities WHERE userId = %s AND dateDue BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_data = []
    for row in result1:
        liabilityCategoryId = row[0]
        dateDue = row[1]

        cursor.execute("SELECT liabilityName, grossAmount, remainingAmount FROM liabilitiesCategory WHERE id = %s", (liabilityCategoryId,))
        result2 = cursor.fetchall()
        liabilityName = result2[0][0]
        grossAmount = result2[0][1]
        remainingAmount = result2[0][2]

        report_data.append({
            "liabilityName": liabilityName,
            "grossAmount": grossAmount,
            "remainingAmount": remainingAmount,
            "dateDue": dateDue
        })
    total_remaining = sum([data['remainingAmount'] for data in report_data])
    total_Gross = sum([data['grossAmount'] for data in report_data])
    total_liabilities = total_Gross - total_remaining
    total_liabilities = ({total_liabilities})
    total_liabilities = total_liabilities.pop()  #parsing it as a float

    cursor.close()
    return report_data, total_liabilities
# print(liabilitiesRawData(2, '2024-05-01', '2024-5-31')) #testing the function
