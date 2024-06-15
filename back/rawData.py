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


# print(expensesRawData(2, '2024-05-01', '2024-6-30')) #testing the function
