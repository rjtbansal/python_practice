import smtplib

host = "smtp.gmail.com"
port = 587
username = ""
password = ""
from_email = username
to_list = ["doej67514@gmail.com","rjtbansal@gmail.com"]

email_conn = smtplib.SMTP(host, port) #connecting to the smtp server
email_conn.ehlo() #identify yourself to esmptp server..smtpmail() implicitly calls this ehlo method
email_conn.starttls() #start tls that will encrypt calls to SMTP
email_conn.login(username, password) #login with username and password
email_conn.sendmail(from_email, to_list, "Hello there this is an email message") 
email_conn.quit() #quitting the connection..i.e logging out

#2nd method 
from smtplib import SMTP #directly importing SMTP class from smtplib
ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "Hello there this is an email message")
ABC.quit()

#exception handling..importing specific exceptions from smtplib documentation
from smtplib import SMTP, SMTPAuthenticationError, SMTPException 

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong_password")
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

pass_wrong.quit()
