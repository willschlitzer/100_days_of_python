from datetime import datetime, date

def showDateInts():
    '''Function to show that the datetime class can return int values'''
    todaydate = datetime.today()
    # Creates int values from the datetime object
    print(todaydate.day)
    print(todaydate.month)
    print(todaydate.year)

def createDate():
    '''Shows how math can be done with date variables'''
    # Assigns date object using only day month year
    todaydate = date.today()
    # Creates a date object
    christmas = date(2020, 12, 25)
    # Completes subtraction between the two dates
    print(christmas - todaydate)

#print(datetime.today())
#showDateInts()
createDate()