
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
    result, data = mail.uid('search', None, '(FROM "Deepak.Khanna@niituniversity.in")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 1..")
    else:
        print("%d emails found of Deepak Khanna, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()

    result, data = mail.uid('search', None, '(HEADER Subject "Newsletter")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 2..")
    else:
        print("%d emails found of Newsletter, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()

    result, data = mail.uid('search', None, '(TO "noc17-hs02-discuss@nptel.iitm.ac.in")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 3..")
    else:
        print("%d emails found of NPTEL Soft Skills, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()

    result, data = mail.uid('search', None, '(FROM "Library@niituniversity.in")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 4..")
    else:
        print("%d emails found of Library, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
    
    result, data = mail.uid('search', None, '(HEADER Subject "lost" FROM "Office.Student.Affairs@niituniversity.in")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 5..")
    else:
        print("%d emails found of Lost things by Office Dean, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
        
    result, data = mail.uid('search', None, '(HEADER Subject "lost" FROM "Ashok.Singh@niituniversity.in")')
    datam = data[0].split()

    if len(datam) == 0:
        print("No emails Found, Finishing 6..")
    else:
        print("%d emails found of Lost things by A.K. Singh, sending to trash folder..." % len(datam))
        for uid in datam: 
            mail.uid('STORE',uid, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")

mail.close()
mail.logout()
print("Done")
