import pywhatkit
import datetime
import time

# Set the phone number and message content
phone_number = "+918484863242"
message = "Happy birthday! 🎉🎂"

# Get today's date
today = datetime.date.today()

# Set the birthday date
birthday_date = datetime.date(today.year, 7, 11)  # Replace with your desired birthday date

# Check if today is the birthday
if today == birthday_date:
    # Calculate the scheduled time with a delay of 1 minute
    scheduled_time = datetime.datetime.now() + datetime.timedelta(minutes=1)

    # Convert the scheduled time to hour and minute
    scheduled_hour = scheduled_time.hour
    scheduled_minute = scheduled_time.minute

    # Send the birthday message
    pywhatkit.sendwhatmsg(phone_number, message, scheduled_hour, scheduled_minute, wait_time=30)
    time.sleep(5)  # Additional delay to allow WhatsApp Web to load

    print("Birthday message sent!")
else:
    print("Today is not the birthday.")
