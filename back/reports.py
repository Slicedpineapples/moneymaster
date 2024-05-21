from server import connect
from utils import Date, makeDir
import datetime
import flask

makeDir() 

def incomeReport(userId, start, end):
    income = connect()
    cursor = income.cursor()

    cursor.execute("SELECT sourceAmountId, incomeCategoryId, date FROM income WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_path = f'reports/IncomeReports/IR-UID-{userId}-{start}-to-{end}.txt'
    with open(report_path, "w") as report_file:
        report_file.write(f'Income report starting {start} to {end}\n')
        report_file.write("Source\tAmount\tCategory\tDate\n")

        report_data = []
        for row in result1:
            sourceAmountId = row[0]
            incomeCategoryId = row[1]
            date = row[2]

            cursor.execute("SELECT sourceName, amount FROM incomeSource WHERE id = %s", (sourceAmountId,))
            result2 = cursor.fetchall()
            sourceName = result2[0][0]
            amount = result2[0][1]

            cursor.execute("SELECT incomeName FROM incomeCategory WHERE id = %s", (incomeCategoryId,))
            result3 = cursor.fetchall()
            incomeName = result3[0][0]

            report_file.write(f"{sourceName}\t{amount}\t{incomeName}\t{date}\n")

            report_data.append({
                "sourceName": sourceName,
                "amount": amount,
                "incomeName": incomeName,
                "date": date
            })

    return report_path, report_data

    #report_file.write(f'\nTotal income: {sum([row[1] for row in result2])}\n')
    report_file.write(f'Report generated for user {userId} on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    report_file.close()
    cursor.close()
    print("Income report generated successfully!\nIt is accessible in the income reports directory.")
    #send report to email address

def expensesReport(userId, start, end):
    start = start
    end = end
    userId = userId
    expenses = connect()
    cursor = expenses.cursor()

    cursor.execute("SELECT expenseCategoryId, expensesPriceId, date FROM expenses WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_path = f'reports/ExpensesReports/ER-UID-{userId}-{start}-to-{end}.txt'
    with open(report_path, "w") as report_file:
        report_file.write(f'Expenses report starting {start} to {end}\n')
        report_file.write("Category\tItem name\tPrice\tDate\n")

        report_data = []
        for row in result1:
            expenseCategoryId = row[0]
            expensesPriceId = row[1]
            date = row[2]

            cursor.execute("SELECT expenseName FROM expensesCategory WHERE id = %s", (expenseCategoryId,))
            result2 = cursor.fetchall()
            expenseName = result2[0][0]

            cursor.execute("SELECT itemName, Price FROM expensesPrice WHERE id = %s", (expensesPriceId,))
            result3 = cursor.fetchall()
            itemName = result3[0][0]
            price = result3[0][1]

            report_file.write(f"{expenseName}\t{itemName}\t{price}\t{date}\n")

            report_data.append({
                "expenseName": expenseName,
                "itemName": itemName,
                "price": price,
                "date": date
            })

        report_file.write(f'\nReport generated for user {userId} on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    cursor.close()
    return report_path, report_data

def assetsReport(userId, start, end):
    userId = userId
    start = start
    end = end

    assets = connect()
    cursor = assets.cursor()

    cursor.execute("SELECT assetCategoryId, value, date FROM assets WHERE userId = %s AND date BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_path = f'reports/AssetsReports/AR-UID-{userId}-{start}-to-{end}.txt'
    with open(report_path, "w") as report_file:
        report_file.write(f'Assets report starting {start} to {end}\n')
        report_file.write("Location\tAsset Name\tValue\tNumber of Items\tDate\n")

        report_data = []
        for row in result1:
            assetCategoryId = row[0]
            value = row[1]
            date = row[2]

            cursor.execute("SELECT assetName, numberOfItems, location FROM assetsCategory WHERE id = %s", (assetCategoryId,))
            result2 = cursor.fetchall()
            assetName = result2[0][0]
            numberOfItems = result2[0][1]
            location = result2[0][2]

            report_file.write(f"{location}\t{assetName}\t{value}\t{numberOfItems}\t{date}\n")

            report_data.append({
                "location": location,
                "assetName": assetName,
                "value": value,
                "numberOfItems": numberOfItems,
                "date": date
            })

        report_file.write(f'\nReport generated for user {userId} on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    cursor.close()
    return report_path, report_data

def liabilitiesReport(userId, start, end):
    userId = userId
    start = start
    end = end

    liabilities = connect()
    cursor = liabilities.cursor()

    cursor.execute("SELECT liabilityCategoryId, dateDue FROM liabilities WHERE userId = %s AND dateDue BETWEEN %s AND %s", (userId, start, end))
    result1 = cursor.fetchall()

    report_path = f'reports/LiabilitiesReports/LR-UID-{userId}-{start}-to-{end}.txt'
    with open(report_path, "w") as report_file:
        report_file.write(f'Liabilities report starting {start} to {end}\n')
        report_file.write("Liability\tGross Amount\tRemaining Amount\tDate Due\n")

        report_data = []
        for row in result1:
            liabilityCategoryId = row[0]
            dateDue = row[1]

            cursor.execute("SELECT liabilityName, grossAmount, remainingAmount FROM liabilitiesCategory WHERE id = %s", (liabilityCategoryId,))
            result2 = cursor.fetchall()
            liabilityName = result2[0][0]
            grossAmount = result2[0][1]
            remainingAmount = result2[0][2]

            report_file.write(f"{liabilityName}\t{grossAmount}\t{remainingAmount}\t{dateDue}\n")

            report_data.append({
                "liabilityName": liabilityName,
                "grossAmount": grossAmount,
                "remainingAmount": remainingAmount,
                "dateDue": dateDue
            })

        report_file.write(f'\nReport generated for user {userId} on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    cursor.close()
    return report_path, report_data


# incomeReport(1)
# expensesReport(1)
# assetsReport(1)
# liabilitiesReport(1)