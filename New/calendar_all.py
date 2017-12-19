import calendar

def year_calendar(year):
    print ("Calendar for the year {0} - {1}".format(year,calendar.calendar(year)))

def month_calendar(year,month):
    print ("Calendar for the month - {0}".format(calendar.month(year,month)))

def current_leap(year):
    print ("Is year {0} leap ? - {1}".format(year,calendar.isleap(year)))


def leap_days(year1,year2):
    print ("Leap days between year {0} and {1} are - {2}".format(year1,year2,calendar.leapdays(year1,year2)))


class day_of_month():

    def week_day(year,month,date):
        day = day_of_month.date(year,month,date)
        print ("Day on year {0}, month {1}, date {2}  - {3}".format(year,month,date,day))


    def date(y,m,d):
        if (calendar.weekday(y,m,d) == 0):
            return "Monday"
        elif (calendar.weekday(y,m,d) == 1):
            return "Tuesday"
        elif (calendar.weekday(y,m,d) == 2):
            return "Wednesday"
        elif (calendar.weekday(y,m,d) == 3):
            return "Thursday"
        elif (calendar.weekday(y,m,d) == 4):
            return "Friday"
        elif (calendar.weekday(y,m,d) == 5):
            return "Saturday"
        elif (calendar.weekday(y,m,d) == 6):
            return "Sunday"


a1 = int(input("Enter year to get year calendar - "))
year_calendar(a1)
print ("\n")

a2,a3 = map(int,input("Enter year and month to get month calendar - ").split())
month_calendar(a2,a3)
print ("\n")

a4 = int(input("Enter year to check if it is a leap year - "))
current_leap(a4)
print ("\n")

a5,a6 = map(int,input("Enter year 1 and year 2 to get leap days between them - ").split())
leap_days(a5,a6)
print ("\n")

a7,a8,a9 = map(int,input("Enter year,month and date to check day - ").split())
day_of_month.week_day(a7,a8,a9)
