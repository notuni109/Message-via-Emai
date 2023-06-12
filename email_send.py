import ast
import os
import content
import datetime
import smtplib
from email.message import EmailMessage
import GUI

class DailyDigestEmail:

    def __init__(self):
        self.quote = content.get_random_quote()
        self.number = content.get_random_number()
        self.link = content.get_random_link()

        self.sender_file = open('sender.txt').read()
        self.sender = ast.literal_eval(self.sender_file)

        self.recipient_file = open('recipient.txt').read()
        self.recipient = [self.recipient_file]
        
    def send_email(self):
        msg = EmailMessage()
        msg['Subject'] = f"Hello There - {datetime.date.today().strftime('%d %b %Y')}"
        msg['From'] = self.sender['email']
        msg['To'] = ', '. join(self.recipient)

        msg_body = self.format_message()
        msg.add_alternative(msg_body, subtype='html')

        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(self.sender['email'], self.sender['password'])
            smtp_server.sendmail(self.sender['email'], self.recipient, msg.as_string())
            print("E-mail sent!")

    def format_message(self):
        html = f"""<html>
    <body>
    <center>
        <h1>Hello There</h1>
        <h1>Your Daily Dose of Shitposts</h1>
        <h1>{datetime.date.today().strftime('%d %b %Y')}</h1>
        <h2>Random Quote of the Day</h2>
        <p>"{self.quote['quote']}" - {self.quote['author']}</p>
        <h2>Lucky Number</h2>
        <p>{self.number}</p>
        <h2>Today you're literally</h2>
        <img src="{self.link[0]}" height="200" width="300" style="display:block">
    </center>
    </body>
</html>
                """
        return html

def main():
        email = DailyDigestEmail()
        message = email.format_message()

        # Write an HTML file
        with open('html_message.html', 'w', encoding='utf-8') as f:
            f.write(message)

        print('Sending E-mail...')
        email.send_email()

        os.remove('D:/Learning/Projects/Message via Emai/sender.txt')
        os.remove('D:/Learning/Projects/Message via Emai/recipient.txt')

if __name__ == '__main__':
    GUI.main()
    