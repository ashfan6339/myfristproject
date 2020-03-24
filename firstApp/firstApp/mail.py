
import smtplib
import imghdr
from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'My Bike'
msg['From'] = 'shaikashfan3@gmail.com'
msg['To'] = 'shaikashfan3@gmail.com'
msg.set_content('yahamaMT15')

with open('12.jpg','rb')as f: 
    file_data =f.read()
    file_type =imghdr.what(f.name)
    file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
     smtp.login('shaikashfan3@gmail.com ', '8247550464')
     smtp.send_message(msg)
