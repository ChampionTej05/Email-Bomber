# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:50:54 2019

@author: champion
"""

    

from tkinter import *
import backend as be
import sys


def submit_details():
    
    server=mailServer_text.get()
    user=fromEmail_text.get()
    passwd=password_text.get()
    to=toEmail_text.get()
    subject=subject_text.get()
    body=body_text.get()
    
    
    if len(server)==0 or len(user)==0 or len(passwd)==0 or len(to)==0 or len(subject)==0 or len(body)==0:
        print("Please Fill ot all the Details,Correctly")
    else:
        try :
            freq=int(freq_text.get())
            print("Details submitted Successfully")
            be.bomb_email(server,user,passwd,to,subject,body,freq)
        except ValueError:
            print("Please Provide Frequency in Natural Numbers")
        
        #print(server+" "+user+" "+passwd+" "+to+" "+subject+" " +body+" " +str(freq))
        
    
        #sys.exit()



window=Tk()

window.wm_title("CHAMPION_TEJ")

#-------------------- Labels For the Program

lb_mailServer=Label(window,text="Mail Server",bd=5,fg="black")
lb_mailServer.grid(row=0,column=0)

lb_toEmail=Label(window,text="To Email",bd=5,fg="black")
lb_toEmail.grid(row=0,column=2)

lb_fromEmail=Label(window,text="From Email ",bd=5,fg="black")
lb_fromEmail.grid(row=1,column=0)

lb_password=Label(window,text="Password",bd=5,fg="black")
lb_password.grid(row=1,column=2)

lb_subject=Label(window,text="Subject",bd=5,fg="black")
lb_subject.grid(row=2,column=0)

lb_body=Label(window,text="Body",bd=5,fg="black")
lb_body.grid(row=2,column=2)

lb_freq=Label(window,text="Frequency",bd=5,fg="black")
lb_freq.grid(row=3,column=0)

#------------------------------------

#---------- Entry Boxes
mailServer_text=StringVar()
en_mailServer_text=Entry(window,textvariable=mailServer_text,bd=5)
en_mailServer_text.grid(row=0,column=1)

toEmail_text=StringVar()
en_toEmail_text=Entry(window,textvariable=toEmail_text,bd=5)
en_toEmail_text.grid(row=0,column=3)

fromEmail_text=StringVar()
en_fromEmail_text=Entry(window,textvariable=fromEmail_text,bd=5)
en_fromEmail_text.grid(row=1,column=1)

password_text=StringVar()
en_password_text=Entry(window,textvariable=password_text,bd=5,show="*")
en_password_text.grid(row=1,column=3)


subject_text=StringVar()
en_subject_text=Entry(window,textvariable=subject_text,bd=5)
en_subject_text.grid(row=2,column=1)

body_text=StringVar()
en_body_text=Entry(window,textvariable=body_text,bd=5)
en_body_text.grid(row=2,column=3)

freq_text=StringVar()
en_freq_text=Entry(window,textvariable=freq_text,bd=5)
en_freq_text.grid(row=3,column=1)
#-----------------

submit=Button(window,text="Submit ", width=15,command=submit_details,bd=5,bg="#F0E68C",fg="black")
submit.grid(row=3,column=3)

window.mainloop()

