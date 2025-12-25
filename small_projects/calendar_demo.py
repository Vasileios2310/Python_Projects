#This program generates printable text files of monthly calendars for the month and year you enter.

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December')

while True:
    print('Enter the year for the calendar ')
    year_response = input('>> ')
    
    if year_response.isdecimal() and int(year_response) > 0:
        year = int(year_response)
        break
    
    print('Please enter a numeric like 2025')
    continue

while True:
    print('Enter a month for the calendar 1 - 12 ')
    month_response = input('>> ')
    
    if month_response.isdecimal() and (0 < int(month_response) <= 12):
        month = int(month_response)
        break
    
    print('Please enter a numeric from 1 to 12')
    continue

def getCalendarFor(year , month):
    calText = ''

    # Put the month and year at the top of the calendar:
    calText += ('' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'  
    
    # Add the days of the week labels to the calendar:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'
 
    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'
    
    currentDate = datetime.date(year , month , 1)
    
    while currentDate.weekday() != 6: 
        currentDate -= datetime.timedelta(days=1)
        
    while True:
        calText += weekSeparator
        
         # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' +dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'
        
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
            
        if currentDate.month != month:
            break
        
    calText += weekSeparator
    return calText


calText = getCalendarFor(year , month)
print(calText)

calendarFilename = 'calendar_{}_{}.txt'.format(year , month)
with open(calendarFilename , 'w')as fileObj:
    fileObj.write(calText)
         
print('Saved to ' + calendarFilename)
    