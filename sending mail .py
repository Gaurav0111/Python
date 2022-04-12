import smtplib
HOST = "smtp.google.com"
SUBJECT = "Test an email"
TO  = "garwalgaurav019@gmail.com"
FROM = "garwalgaurav1@gmail.com"
text = "blah blah blah"
BODY = "\r\n".join((
    f"From : {FROM}",
    f"To : {TO}",
    f"SUBJECT : {SUBJECT} ",
    "",
    text)
)
server = smtplib.SMTP(HOST)
server.sendmail(FROM,[TO],BODY)
server.quit()