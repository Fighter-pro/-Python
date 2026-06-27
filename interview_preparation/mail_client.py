

import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailClient:

    def __init__(
            self,
            login,
            password,
            smtp_server='smtp.gmail.com',
            imap_server='imap.gmail.com',
            smtp_port=587
    ):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.smtp_port = smtp_port

    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp_client:
            smtp_client.ehlo()
            smtp_client.starttls()
            smtp_client.ehlo()
            smtp_client.login(self.login, self.password)
            smtp_client.sendmail(self.login, recipients, msg.as_string())

    def receive_message(self, folder='inbox', header=None):
        with imaplib.IMAP4_SSL(self.imap_server) as mail_client:
            mail_client.login(self.login, self.password)
            mail_client.select(folder)

            if header:
                criterion = f'(HEADER Subject "{header}")'
            else:
                criterion = 'ALL'

            result, data = mail_client.uid('search', None, criterion)

            if not data[0]:
                raise ValueError('There are no letters with current header')

            latest_email_uid = data[0].split()[-1]
            result, data = mail_client.uid(
                'fetch',
                latest_email_uid,
                '(RFC822)'
            )

            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'password'

    mail_client = MailClient(login, password)

    # Пример отправки письма:
    # mail_client.send_message(
    #     recipients=['vasya@email.com', 'petya@email.com'],
    #     subject='Subject',
    #     message='Message'
    # )

    # Пример получения письма:
    # email_message = mail_client.receive_message(header=None)
    # print(email_message)

