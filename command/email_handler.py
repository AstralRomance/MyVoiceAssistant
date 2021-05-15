# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


class EmailSender:
    def __init__(self, email_address, password, smtp_host, smtp_port):
        self._server = smtplib.SMTP(smtp_host, smtp_port)
        self._email = email_address
        self._password = password

    def send(self, to_email, title, msg_text):
        msg = self._build_a_message(to_email, title, msg_text)
        self._server.ehlo()  # Кстати, зачем это?
        self._server.starttls()
        self._server.login(self._email, self._password)
        self._server.send_message(msg)

    def _build_a_message(self, to_email, title, msg_text):
        msg = EmailMessage()
        msg.set_content(msg_text)
        msg['Subject'] = title
        msg['From'] = self._email
        receiver = to_email
        if type(to_email) == list:
            receiver = ",".join(to_email)
        msg['To'] = receiver
        return msg
