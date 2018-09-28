import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders

def send_mail(send_from, send_to, subject, files=None,
              server="smtp.gmail.com:587"):
    try:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("abc.xlsx", "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename='abc.xlsx')
        encoders.encode_base64(part)
        msg.attach(part)
        smtp = smtplib.SMTP(server)
        smtp.ehlo()
        smtp.starttls()
        smtp.login("sowmyasrinivas789@gmail.com", "sow789SS@")
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
    except Exception as e:
        print(e)

send_mail("sowmyasrinivas789@gmail.com", ["vivekshahi30@gmail.com"], "subject: test")
