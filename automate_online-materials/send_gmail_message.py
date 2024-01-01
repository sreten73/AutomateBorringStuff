import smtplib
import datetime
import getpass

sender_email = "sreten7398@gmail.com"
receiver_email = "sreten98@gmail.com"
# feem mvas tyqy iyaw
#dzabxbisxfzccclh
password = getpass.getpass("Enter your APP password: ")
today = datetime.date.today()
message = f"""\
Subject: Always new message

Hello,
this is the new message.
 Today is  {today}
Regards,
Sreten
"""

# connect to Gmail's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

# send the email
server.sendmail(sender_email, receiver_email, message)
print("Email sent successfully!")

# close the connection to the server
server.quit()
