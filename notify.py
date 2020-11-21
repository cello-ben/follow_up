from email.mime.text import MIMEText
import smtplib
import sqlite3
import datetime
import yaml

with open('app.yaml') as file:
    env = yaml.load(file, Loader = yaml.FullLoader)['env_variables']

conn = sqlite3.connect('follow_ups.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM flw_ups')
list = cursor.fetchall()

followup_list = ''
for i in list:
    if i[2] == str(datetime.datetime.today().toordinal()):
        followup_list += (str(i[1]) + ' ')

SMTP_SERVER = env['SMTP_SRV']
SMTP_PORT = 587
SMTP_USERNAME = env['SMTP_USER']


if followup_list != '':
    SMTP_PASSWORD = env['SMTP_PASS']
    EMAIL_TO = [[env['EMAIL_T']]]
    EMAIL_FROM = env['EMAIL_F']
    EMAIL_SUBJECT = 'Today\'s Follow-Up Reminders'

    DATA = 'Good morning, (your name)! Today, you need to follow up with the following people: ' + followup_list

    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()
