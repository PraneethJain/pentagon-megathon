import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(receiver_email: str, message: str, subject: str = "Results of the Psyche-Screener Test") -> None:
    sender_email = "bbcprolab@gmail.com"

    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg['subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    smtp_server = "smtp.gmail.com" 
    smtp_port = 587 
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, "ahsm yutl iuxp smyq") 

        server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()

        print("email sent successfully")

    except Exception as e:
        print(f"email sending failed: {str(e)}")
