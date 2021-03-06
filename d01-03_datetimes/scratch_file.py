from datetime import datetime, date, timedelta


def showDateInts():
    """Function to show that the datetime class can return int values"""
    todaydate = datetime.today()
    # Creates int values from the datetime object
    print(todaydate.day)
    print(todaydate.month)
    print(todaydate.year)


def dateMath():
    """Shows how math can be done with date variables"""
    # Assigns date object using only day month year
    todaydate = date.today()
    # Creates a date object
    christmas = date(2020, 12, 25)
    # Completes subtraction between the two dates
    # .days method returns only subtraction using days
    christmas_days = (christmas - todaydate).days
    if christmas is not todaydate:
        print("There are still " + str(christmas_days) + " days until Christmas!")
    else:
        print("Today is Christmas!")


def exploreTimeDelta():
    """Create timedelta object and add it to date object"""
    t = timedelta(days=4, hours=10)
    eta = timedelta(hours=6)
    today = datetime.today()
    # Shows additions of the timedelta to a date object
    print(eta)
    print(today + t)


def countdownSubtraction():
    end = datetime(2020, 6, 18, 18, 30, 0, 0)
    rightnow = datetime.today()
    togo = end - rightnow
    print(togo)
    print(type(togo))
    print(togo.days)


def elapsedPercentCalc():
    end = datetime(2020, 6, 18, 18, 30, 0, 0)
    start = datetime(2020, 1, 11, 11, 43, 0, 0)
    totaltime = end - start
    right_now = datetime.today()
    completedtime = right_now - start
    print(type(completedtime))
    print(completedtime / totaltime)


def test_timedelta_running():
    """Test to see that a timedelta object is viewed the same as a subtraction of two values"""
    end = timedelta(seconds=10)
    start = datetime.today()
    running = True
    while running:
        if (datetime.today() - start) == end:
            print("Time's Up")
            running = False


def test_timedelta_inputs():
    """Test different inputs for timedelta"""
    a = timedelta(minutes=5)
    b = timedelta(hours=10)
    print(a.seconds)


def test_date_string():
    """Creating test for using strptime method"""
    mydate = datetime.strptime("10 Aug, 2020", "%d %b, %Y")
    print(mydate)
    datestring = datetime.strftime(mydate, "%B %d, %Y")
    print(datestring)


# print(datetime.today())
# showDateInts()
# dateMath()
exploreTimeDelta()
# countdownSubtraction()
# elapsedPercentCalc()
# test_timedelta_running()
# test_timedelta_inputs()
# test_date_string()
