
# using python to know what a function does 
print(abs.__doc__)

# get the calendar for any month and year
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# how to print in multiple lines without using escape sequence 
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
