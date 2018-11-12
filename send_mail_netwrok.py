import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
server="outlook.toshiba-tsip.com"
send_from = "sowmya.srinivas@toshiba-tsip.com"

def send_mail(send_from, send_to, subject, files=None,
              server=server):
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
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
    except Exception as e:
        print(e)

send_mail(send_from, ["Prajwal.Jagannatha@toshiba-tsip.com", "Rohini.chougule@toshiba-tsip.com", "Ruthvi.Nagarajan@toshiba-tsip.com"], "subject: test")
