#Part 2:
#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
#Write a Python program to solve the general version of the above problem. Ask the user for the 
#time now (in hours) and then ask for the number of hours to wait for the alarm. Your program should 
#output what the time will be on a 24-hour clock when the alarm goes off.

# Display a guide for the 24-hour clock scale
print("Guide to the 24-hour clock (Military Time):")
print("00:00 to 11:59 - AM hours (00:00 is midnight, 11:00 is 11AM)")
print("12:00 to 23:59 - PM hours (12:00 is noon, 23:00 is 11PM)")
print("Please enter times in the 24-hour format. For example, 3 PM is 15:00.\n")

# Prompt the user for the present hour and duration to set the alarm
present_hour = int(input("Enter the current hour (0-23) on the 24-hour clock: "))
alarm_set_duration = int(input("Enter the number of hours to set the alarm for: "))

# Store inputs in a list for processing
time_details = [present_hour, alarm_set_duration]

# Calculate when the alarm will sound using list elements
alarm_sound_hour = (time_details[0] + time_details[1]) % 24

# Output the time the alarm will go off
print(f"Alarm will sound at {alarm_sound_hour}:00 on the 24-hour scale.")