import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user = "g7@bmsit.in"
email_password = "yxgcyxfzgdihxowa"
subject = "Attendance alert"


with open('Student_daily_record.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        text = "Hello " + line[0] + ", you were marked present today."
        send_email = line[1]
        print(send_email)
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = send_email
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))

        text = msg.as_string()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Use STARTTLS encryption

        server.login(email_user, email_password)
        print("login successfull")
        server.sendmail(email_user, send_email, text)
        server.quit()