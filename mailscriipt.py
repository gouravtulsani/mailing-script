from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import smtplib

 
fromaddr = "tulsanig1432@gmail.com"
toaddr = str(raw_input("enter sender's mailaddress: "))
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = str(raw_input("Subject: "))

body = str(raw_input("Body: "))
 
msg.attach(MIMEText(body, 'plain'))
attachfile = str(raw_input("Attach a file (y/n)"))
if attachfile == "y":

	filename = str(raw_input("NAME OF THE FILE WITH ITS EXTENSION: "))
	attachment = open(str(raw_input("PATH OF THE FILE: ")), "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "xpgquodognpmeujt")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("mail sent.")