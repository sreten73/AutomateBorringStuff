# Import section
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Gmail configuration
sender_email = "gdcservices01@gmail.com"
sender_alias = "GDC"
sender_password = "mtyyjnwtpeukraxr"
receiver_emails = ["sreten98@gmail.com", "srecko98@gmail.com"]
subject = "Test02"
body = "Here is another test email"

# Files for attachments
attachments = ['C:\\Users\\jokics\\Documents\\JOBS\\GDC\\FTP_Log\\ftp.log']

# Create email
message = MIMEMultipart()
message["From"] = f"{sender_alias}"
message["To"] = ",".join(receiver_emails)
message["Subject"] = subject
message.attach(MIMEText(body,'plain'))

# Attach the files
for attachment in attachments:
    with open(attachment, "rb") as file:
        part = MIMEApplication(file.read())
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment)}")
        message.attach(part)

# Connect to GMAIL SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, receiver_emails, message.as_string())

# Close the connection to SMTP
server.quit()

