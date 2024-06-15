from server import connect
#Making a select querry for income. It will fetch all incomes, then categorice them by category and sum them up.The result will be a list of dictionaries.
def incomeReport(userId, start, end):
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
    total_income = ({"Total" : total_income})

    return report_data, total_income

print(incomeReport(2, '2024-05-01', '2024-5-31'))
