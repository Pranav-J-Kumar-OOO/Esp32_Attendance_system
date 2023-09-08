import smtplib
from email.message import EmailMessage

def sendGmail(appPws:str, From:str, To:str, Subject:str, Body:str):
    msg = EmailMessage()
    msg.set_content(Body)
    msg['Subject'] = Subject
    msg['From'] = From
    msg['To'] = To

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(From, appPws)
        smtp.send_message(msg)