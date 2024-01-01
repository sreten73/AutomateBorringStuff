import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Gmail configuration
sender_email = "gdcservices01@gmail.com"
sender_alias = "GDC"
app_password = "mtyyjnwtpeukraxr"
#receiver_email = "sreten98@gmail.com"
#receiver_email = "sreten.jokic@gdc-services.tech"
#receiver_emails = ["sreten.jokic@gdc-services.tech", "Denis.Gatiyatullin@gdc-services.tech"]
receiver_emails = ["sreten98@gmail.com", "sreten.jokic@gdc-services.tech"]
subject = "Test email with attachments"
body = "This is a test email sent from Python"

# List of the file paths for attachments
attachment_paths = ["C:\\Users\\jokics\\Documents\\JOBS\\GDC\\FTP_Log\\ftp.log", "C:\\Users\\jokics\\Documents\\JOBS\\GDC\\FTP_Log\\log_check_files.txt"]

# Create the mail
message = MIMEMultipart()
#message["From"] = sender_email
#message["From"] = f"{sender_alias} <{sender_email}>"
message["From"] = f"{sender_alias}"
message["To"] = ",".join(receiver_emails)
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Attach the files
for attachment_path in attachment_paths:
    with open(attachment_path, "rb") as attachment_file:
        part = MIMEApplication(attachment_file.read())
        part.add_header(
            "Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}"
        )
        message.attach(part)

# Connect to GMAIL's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email,app_password)

# Send the email
#server.sendmail(sender_email,receiver_email,message.as_string())

#receiver_email = "denis.Gatiyatullin@gdc-services.tech"
#message["To"] = receiver_email
server.sendmail(sender_email,receiver_emails,message.as_string())

# Send the email to each recipient
#for receiver_email in receiver_emails:
#    message["To"] = receiver_email
#    server.sendmail(sender_email,receiver_email,message.as_string())

# Close the connection
server.quit()