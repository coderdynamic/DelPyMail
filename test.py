
import imaplib, email, sys
from imaplib import *

#Account Credentials
username = 'username@gmail.com'
password = 'password'

print("Logging into your Gmail Account...")

mail = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    mail.login(username,password)
    print("Logged IN!!")
    mail.list()
    mail.select("inbox")
    result, data = mail.uid('search', None, '(FROM "username2@gmail.com")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 1..")
    else:
        print("%d emails found, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()

    result, data = mail.uid('search', None, '(HEADER Subject "Subject")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 2..")
    else:
        print("%d emails found, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()

    result, data = mail.uid('search', None, '(TO "username3@gmail.com")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 3..")
    else:
        print("%d emails found , sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
    
    result, data = mail.uid('search', None, '(HEADER Subject "Subject" FROM "username4@gmail.com")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 4..")
    else:
        print("%d emails found, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
       
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")

mail.close()
mail.logout()
print("Done")
