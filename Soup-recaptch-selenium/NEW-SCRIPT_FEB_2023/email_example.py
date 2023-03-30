
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

receivers_mail = ['rk2153691@gmail.com','rksingh@nextgenesolutions.com','nkmishra@nextgenesolutions.com']
# cc= ['devanshu@nextgenesolutions.com']
msg = MIMEMultipart()
msg['From'] = 'sales@raptorsupplies.com'
msg['To'] = receivers_mail
# msg['Cc'] = cc

toAddress = msg['To']
subject = "INDEX FOLLOW Header Check"
body = "INDEX FOLLOW Header Check"
massage="subject:{}\n\n{}".format(subject,body)
server = smtplib.SMTP("email-smtp.eu-west-1.amazonaws.com",587)
server.starttls()
server.login("AKIAROILJ6GGW4CGS57B", "BM/Jl5EwExQ/8/xER6HEJH+tiWSr9eLUW+eZUlPEqyKU")
server.sendmail(msg['From'], toAddress, massage)
print('send email')
server.quit()


