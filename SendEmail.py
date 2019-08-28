'''
Example of automation
Sends email to a person through the terminal
Some code snippets taken from:
https://github.com/ginigangadharan/scripts/blob/master/python-email.py
https://automatetheboringstuff.com/chapter16/
'''
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_providers = {
	"Gmail": "smtp.gmail.com",
	"Outlook.com/Hotmail.com": "smtp-mail.outlook.com",
	"Yahoo Mail": "smtp.mail.yahoo.com",
	"AT&T": "smtp.mail.att.net", # port 465
	"Comcast": "smtp.comcast.net",
	"Verizon": "smtp.verizon.net" # port 465
}
email_smtp_port = 587
chosen_email_provider = False
email_provider = ""
while chosen_email_provider == False:
	email_provider = input("Choose your email provider:\nGmail\nOutlook.com/Hotmail.com\nYahoo Mail\nAT&T\nComcast\nVerizon\n")
	if email_provider in email_providers:
		if email_provider == "AT&T" or email_provider == "Verizon":
			email_smtp_port = 465
		email_provider = email_providers[email_provider]
		chosen_email_provider = True
	else:
		print("This email provider doesn't exist!")

print("Authentication")
print("--------------")
email_from_addr = input("Enter your email:")
your_password = getpass.getpass("Enter your password:")
email_to_addr = input("Enter recipient email:")
email_subject = input("Enter the subject:")
msg = input("Write down your message:")
email_body = "<html><header></header><body><p>"+ msg + "</p></body></html>"

# first, connect to a smtp server
server = smtplib.SMTP(email_provider, email_smtp_port)
# If you are not connected to the Internet, Python will raise a socket.gaierror: [Errno 11004] getaddrinfo failed or similar exception.
server.ehlo()
# Using TLS encryption
server.starttls()
# Log into your smtp account
# 235 = authentication successful
# smtplib.SMTPAuthenticationError for incorrect passwords
server.login(email_from_addr, your_password)
# Time to send the email!
message = MIMEMultipart('alternative')
message['From'] = email_from_addr
message['To'] = email_to_addr
message['Subject'] = email_subject
body = email_body
message.attach(MIMEText(body, 'html'))
text = message.as_string()
server.sendmail(email_from_addr, email_to_addr, message.as_string())
print("Email was successfully sent!")
# close connection
server.quit()