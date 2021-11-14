import smtplib
from email.message import EmailMessage
import imghdr
from string import Template


def get_contacts(filename):
    names = []
    emails_to = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails_to.append(a_contact.split()[1])
    return names, emails_to


email_add = 'champion300102@gmail.com'
password_me = 'atikin123'

name, to = get_contacts('LetsBuild.png', 'python.png')
for i in range(len(to)):
    msg = EmailMessage()
    msg['Subject'] = 'PYTHON WORLD'
    msg['From'] = email_add
    msg['to'] = to[i]
    msg.set_content(f"Hello {name[i]}")
    File = ['Sachin Gujjar DBMS assignment.pdf']
#  THIS IS FOR PDF
    # for file in File:
    #     with open(file, 'rb') as imgp:
    #         file_data = imgp.read()
    #         file_name = imgp.name
    #
    #     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# THis is for images
    for file in File:
        with open(file, 'rb') as imgp:
            file_data = imgp.read()
            file_type = imghdr.what(imgp.name)
            file_name = imgp.name

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_add, password_me)
        smtp.send_message(msg)


