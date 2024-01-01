import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Gmail configuration
sender_email = "gdcservices01@gmail.com"
app_pass = "mtyyjnwtpeukraxr"
receiver_email = "sreten98@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python"

# Create email
message =MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Sybject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to GMAIL's SMTP server
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email, app_pass)

# Send test email
server.sendmail(sender_email, receiver_email, message.as_string())

# Close the connection
server.quit()