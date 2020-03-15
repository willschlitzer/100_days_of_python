from datetime import datetime, date


def showDateInts():
    """Function to show that the datetime class can return int values"""
    todaydate = datetime.today()
    # Creates int values from the datetime object
    print(todaydate.day)
    print(todaydate.month)
    print(todaydate.year)


def createDate():
    """Shows how math can be done with date variables"""
    # Assigns date object using only day month year
    todaydate = date.today()
    # Creates a date object
    christmas = date(2020, 12, 25)
    # Completes subtraction between the two dates
    # .days method returns only subtraction using days
    christmas_days = ((christmas - todaydate).days)
    if christmas is not todaydate:
        print("There are still " + str(christmas_days) + " days until Christmas!" )
    else:
        print("Today is Christmas!")


# print(datetime.today())
# showDateInts()
createDate()
