#Exercise 1: Print Current Date and Time
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

#Exercise 2: Format DateTime
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%d-%b-%Y %I:%M:%S %p")
print("Formatted:", formatted)

#Exercise 3: Convert String Into Datetime Object
from datetime import datetime
date_string = "20 January, 2025"
dt = datetime.strptime(date_string, "%d %B, %Y")
print("DateTime object:", dt)

#Exercise 4: Combine Date and Time Objects
from datetime import date, time, datetime
d = date(2025, 5, 20)
t = time(9, 45, 0)
combined = datetime.combine(d, t)
print("Combined datetime:", combined)

#Exercise 5: Print Current Time in Milliseconds
from datetime import datetime
current = datetime.now()
print(current.strftime("%H:%M:%S.%f")[:-3])
