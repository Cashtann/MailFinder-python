
# autho: Maciej Świtała AKA Cashtan


import email
import imaplib
from time import sleep
import os



address = 'imap.gmail.com'
port = 993
login = 'cashtan2137@gmail.com' # Twój mail
password = ' APP PASSWORD do maila ' # app password to nie jest normalne hasło do twojego maila, tylko hasło dla aplikacji
imap = imaplib.IMAP4_SSL("imap.gmail.com")

mail = imaplib.IMAP4_SSL(address)
# print(mail)
login_status, msg = mail.login(login, password)


while True:
    if login_status == 'OK':
        # print("Login successful")
        mail.select('inbox') #  wybor skrzynki
        search_status, data = mail.search(None ,'ALL') #  zestaw znakow, filtr
        mail_list = []
        for block in data:
            mail_list += block.split()
        # print(mail_list)
        for i in mail_list:
            fetch_status, data = mail.fetch(i, '(RFC822)') #  numer ID maila, format maila

            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])

                    msg_from = message['from']
                    msg_subject = message['subject']

                    if message.is_multipart():
                        # https://www.w3.org/Protocols/rfc1341/ etc.
                        msg_content = ''

                        for part in message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                msg_content += part.get_payload()
                    else:
                        msg_content = message.get_payload()

                    msg1 = msg_content.replace(' ','')   
                    msg2 = msg1.replace('\n','') 
                    msg3 = msg2.replace("""
                    """,'') 
                    msg4 = msg3.replace(""" """,'') 
                    msg5 = msg4.replace("""

    """,'')
                    msg6 = msg5.strip()
                    print(msg6.rstrip())
                    with open('collectedmsg.txt', 'a') as y:
                        y.write(str(msg6.strip()))
                        y.close()

                    sleep(3)
                    box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                    box.login(login,password)
                    box.select('Inbox')
                    typ, data = box.search(None, 'ALL')
                    for num in data[0].split():
                        box.store(num, '+FLAGS', '\\Deleted')
                    box.expunge()

                    file53 = open('collectedmsg.txt', 'r+')
                    file54 = file53.readlines()
                    file53.close()
                    file55 = str(file54)
                    if msg6 == 'start':
                        os.system('cmd /k "python main.py"')
                        
                        with open('collectedmsg.txt', 'r+') as file420:
                            file420.truncate(0)
                            file420.close()
                    if msg6 == 'stop':
                        with open('collectedmsg.txt', 'r+') as file420:
                            file420.write('stop')
                            sleep(2)
                            file420.truncate(0)
                            file420.close()    

    else:
        print(login_status, msg)
