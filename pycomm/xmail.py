#! /bin/python
#-*-coding: utf-8-*-
import smtplib
from log import Log
from email.mime.text import MIMEText
from email.utils import formataddr

DOMAIN = "smtp.qq.com"
PORT = 465 

class Xmail(object):
    
    def __init__(self, name, passwd):
        self.client = self.SMTPClient(DOMAIN, PORT)
        self.name = name
        self.passwd = passwd
        self.fromUser = formataddr(["Movie Spider", name])
        self.toUser = formataddr(["FK", name])


    def __del__(self):
        if self.client:
            self.client.quit()

    def SMTPClient(self, domain, port):
        try:
            client = smtplib.SMTP_SSL(domain, port)
            client.login(self.name, self.passwd)

        except:
            Log("check in error", "red")
            client = None

        return client

    def SendMail(self, Subject, msg):
        msg = MIMEText(msg, "plain", "utf-8")
        
        msg["from"] = self.fromUser
        msg["to"] = self.toUser 
        msg["Subject"] = Subject 

        try:
            self.client.sendmail(self.name, [self.name,], msg.as_string())

        except Exception as e:
            Log(str(e), "red")
            return False

        finally:
            self.client.quit()
            self.client = None

        return True


            
            
       
       
