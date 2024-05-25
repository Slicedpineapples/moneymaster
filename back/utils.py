import datetime
import os
def makeDir():
    folder = 'reports/AssetsReports'
    if not os.path.exists(folder):
        os.makedirs(folder)

    folder = 'reports/LiabilitiesReports'
    if not os.path.exists(folder):
        os.makedirs(folder)

    folder = 'reports/ExpensesReports'
    if not os.path.exists(folder):
        os.makedirs(folder)

    folder = 'reports/IncomeReports'
    if not os.path.exists(folder):
        os.makedirs(folder)

def Date():
    defaultdate = datetime.datetime.now()
    # global month #Debugging only
    year = input("Year: ")
    month = input("Month: ")
    day = input("Day: ")

    if (year == "" and month == "" and day == ""):
        date = datetime.datetime(defaultdate.year, defaultdate.month, defaultdate.day)
        month = defaultdate.month
    elif (year == "" and month == "" and day != ""):
        date = datetime.datetime(defaultdate.year, defaultdate.month, int(day))
        month = defaultdate.month
    elif (year == "" and month != "" and day == ""):
        date = datetime.datetime(defaultdate.year, int(month), defaultdate.day)
    elif (year == "" and month != "" and day != ""):
        date = datetime.datetime(defaultdate.year, int(month), int(day))
    elif (year != "" and month == "" and day == ""):
        date = datetime.datetime(int(year), defaultdate.month, defaultdate.day)
        month = defaultdate.month
    elif (year != "" and month == "" and day != ""):
        date = datetime.datetime(int(year), defaultdate.month, int(day))
        month = defaultdate.month
    elif (year != "" and month != "" and day == ""):
        date = datetime.datetime(int(year), int(month), defaultdate.day)
    else:
        date = datetime.datetime(int(year), int(month), int(day))
    # print(date, month) # Debugging purpose only

    # # Combining bith functins for ease when calling them in my other procedures

    # month = int(month)
    # # print(f'Month is {month}, from Convert function') #Debugging only
    # month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # # print(month_names[month - 1])  #Debugging only
    # monthName = month_names[month - 1]
    return date
