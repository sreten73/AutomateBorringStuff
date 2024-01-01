import smtplib
import datetime
import getpass

sender_email = input("Enter your email:")
receiver_email = input("Enter the email of the recepient: ")
password = getpass.getpass("Enter your APP password for GMAIL: ")

today = datetime.date.today()

message = f"""
Subject: Always new message

Hello,
this is the new message.
 Today is  {today}
Regards,
MyName
"""

# connect to Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, loz)
    print("Successfully login to gmail.")
except:
    print("Login to gmail failed.Check once again gmail email and APP pass.")

# send the email
try:
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except:
    print("Email didn't sent. There are some errors. PLease see the logs.")

# close the connection to the server
server.quit()
