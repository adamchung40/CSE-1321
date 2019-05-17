today = int(input("Enter today's day (0 for Sunday, 1 for Monday, 2 for Tuesday, etc.) "))
num_days = int(input("Number of days until the next meeting "))
meeting_day = (today + num_days) % 7

if today == 0:
	today = "Sunday"
elif today == 1:
	today = "Monday"
elif today == 2:
	today = "Tuesday"
elif today == 3:
	today = "Wednesday"
elif today == 4:
	today = "Thurday"
elif today == 5:
	today = "Friday"
elif today == 6:
	today = "Saturday"

if meeting_day == 0:
	meeting_day = "Sunday"
elif meeting_day == 1:
	meeting_day = "Monday"
elif meeting_day == 2:
	meeting_day = "Tuesday"
elif meeting_day == 3:
	meeting_day = "Wednesday"
elif meeting_day == 4:
	meeting_day = "Thurday"
elif meeting_day == 5:
	meeting_day = "Friday"
elif meeting_day == 6:
	meeting_day = "Saturday"

#Print Statements
print("Today is ", today)
print("Days to the meeting is " + str(num_days) + " days")
print("Meeting day is", meeting_day)