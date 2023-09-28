from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import datetime
import config
import win32com.client as win32

def send_email_thru_outlook(email_subject, email_body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.success_email["reciever_email_thru_outlook"]
    mail.Subject = email_subject
    mail.Body = email_body
    mail.Send()

def send_final_email_thru_outlook(email_subject, email_body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.success_email["reciever_email_final"]
    mail.Subject = email_subject
    mail.Body = email_body
    mail.Send()

def send_email(subject, body):
    sender_email = config.success_email["sender_email"]
    sender_2fa = config.success_email["sender_2fa"] # configure this after enabling 2fa and then creating new app password
    reciever_email = config.success_email["reciever_email"]
    email_body = body

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    #smtp = smtplib.SMTP('smtp.office365.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_2fa) #using 2fa app pw

    msg = MIMEMultipart()
    msg['Subject'] = subject

    body = MIMEText(email_body, "plain")
    msg.attach(body)
    
    #to = [reciever_email]
    for email in reciever_email:
        smtp.sendmail(from_addr=sender_email,
                to_addrs=[email], msg=msg.as_string())
        print("Sent email to " + email)
    smtp.quit()