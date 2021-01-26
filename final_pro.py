# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:29:41 2020

@author: bharg
"""

import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

con=sqlite3.connect('final_db.db')
cor=con.cursor()


top=tk.Tk()
top.title("Login")
lab_use=tk.Label(top,text="User Name:")
lab_pass=tk.Label(top,text="Password:")
tb_use=tk.Entry(top)
tb_pass=tk.Entry(top,show='*')
lab_dis=tk.Label(top)
def click():
    user=tb_use.get()
    passwd=tb_pass.get()
    
    con=sqlite3.connect('final_db.db')
    cor=con.cursor()

    cor.execute('SELECT * FROM login WHERE user="%s" AND pass="%s"'%(user,passwd))
    if cor.fetchone() is not None:
        messagebox.showinfo("validation","welcom to our family")
        top.destroy()
        main=tk.Tk()
        lab1=tk.Label(main,font=('arial',40,'bold'),text="Shreeji Ad Company",bd=10,fg="blue")
        lab1.grid(row=0,column=12)
        main.title("Shreeji Ad Managment")
        name=tk.Label(main,text="Name:")
        name_en=tk.Entry(main)
        name.grid(row=5,column=0)
        name_en.grid(row=5,column=1)
        val= ["Ahemdabad","Junagadh","Mehsana","Rajkot"] 
        city=tk.Label(main,text="Select city:")
        cb=ttk.Combobox(main,values=val)
        city.grid(row=6,column=0)
        cb.grid(row=6,column=1)
        area=tk.Label(main,text="Select Area:")
        area.grid(row=7,column=0)
        def areaname():
            if cb.get()=="Ahemdabad":
                val1=["Iskon","Maninagar","Prahladnagar","Geeta mandir"]
                cb1=ttk.Combobox(main,values=val1)
                cb1.grid(row=7,column=1)
            elif cb.get()=="Junagadh":
                val1=["Timbawadi","Madhuram","Zanzarda Road","Bhavnath"]
                cb1=ttk.Combobox(main,values=val1)
                cb1.grid(row=7,column=1)
            elif cb.get()=="Mehsana":
                val1=["ONGC Circle","Modhera Circle","Radhanpur Circle"]
                cb1=ttk.Combobox(main,values=val1)
                cb1.grid(row=7,column=1)
            else:
                val1=["Ring Road","Shastri medan","Gokulnagar"]
                cb1=ttk.Combobox(main,values=val1)
                cb1.grid(row=7,column=1)
            
        bt=tk.Button(main,text="Click to get Area",command=areaname)
        bt.grid(row=7,column=2)
        hoarding_size=tk.Label(main,text="Select Size of Hoarding:")
        hoarding_size.grid(row=8,column=0)
        val2=["12 x 6 ft","22 x 10 ft","25 x 12 ft","40 x 12 ft","50 x 20 ft"]
        cb2=ttk.Combobox(main,values=val2)
        cb2.grid(row=8,column=1)
        day=tk.Label(main,text="Enter Days:")
        day_en=tk.Entry(main)
        day.grid(row=9,column=0)
        day_en.grid(row=9,column=1)
        pri=tk.Label(main,text="Total Amount:")
        pri_en=tk.Entry(main)
        def price():
            if cb2.get()=="12 x 6 ft":
                a=int(day_en.get())
                total=a*1200
                v=tk.StringVar()
                v.set(str(total))
                pri_en.config(textvariable=v)
                
            elif cb2.get()=="22 x 10 ft":
                a=int(day_en.get())
                total=a*1600
                v=tk.StringVar()
                v.set(str(total))
                pri_en.config(textvariable=v)
            
            elif cb2.get()=="25 x 12 ft":
                a=int(day_en.get())
                total=a*2200
                v=tk.StringVar()
                v.set(str(total))
                pri_en.config(textvariable=v)
            
            elif cb2.get()=="40 x 12 ft":
                a=int(day_en.get())
                total=a*2500
                v=tk.StringVar()
                v.set(str(total))
                pri_en.config(textvariable=v)
            
            elif cb2.get()=="50 x 20 ft":
                a=int(day_en.get())
                total=a*3000
                v=tk.StringVar()
                v.set(str(total))
                pri_en.config(textvariable=v)
            
            
                
                
        pri_bt=tk.Button(main,text="Click to Show Amount",command=price)
        pri.grid(row=10,column=0)
        pri_en.grid(row=10,column=1)
        pri_bt.grid(row=10,column=2)
        pro=tk.Label(main,text="Product/Company:")
        pro_en=tk.Entry(main)
        ad=tk.Label(main,text="Describe your Ad:")
        ad_box=tk.Text(main,height=3,width=15)
        pro.grid(row=11,column=0)
        pro_en.grid(row=11,column=1)
        ad.grid(row=12,column=0)
        ad_box.grid(row=12,column=1)
        em=tk.Label(main,text="Email id:")
        em_en=tk.Entry(main)
        em.grid(row=13,column=0)
        em_en.grid(row=13,column=1)
        def send_mail():
            sender_email = "bhargavbechara18@gnu.ac.in"
            receiver_email = em_en.get()
            password = "gnu09092000"

            message = MIMEMultipart("alternative")
            message["Subject"] = "Thank you for using our services!!!!!"
            message["From"] = sender_email
            message["To"] = receiver_email

            text = "Shreeji ad company\n hi "+name_en.get()+"\nyour total bill price is "+pri_en.get()
            part1 = MIMEText(text, "plain")
            message.attach(part1)


            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print('ok')
        fin_bt=tk.Button(main,text="Confirm order",command=send_mail)
        fin_bt.grid(row=14,column=0)
        main.mainloop()
    else:
        messagebox.showinfo("validation","Please Insert proper username & password")
   #con.commit()
   #con.close()
def new_reg():
    top.destroy()
    reg_page=tk.Tk()
    reg_page.title("New Registation")
    lab1=tk.Label(reg_page,font=('arial',40,'bold'),text="Shreeji Ad Company",bd=10,fg="blue")
    lab1.grid(row=0,column=12)
    lab=tk.Label(reg_page,text="*Please fill the All Information Properly",fg="red")
    lab.grid(row=34,column=7)
    lab_fn=tk.Label(reg_page,text="Enter First Name: ")
    fn1=tk.Entry(reg_page)
    lab_mn=tk.Label(reg_page,text="Enter Middle Name: ")
    mn1=tk.Entry(reg_page)
    lab_ln=tk.Label(reg_page,text="Enter Last Name: ")
    ln1=tk.Entry(reg_page)
    lab_fn.grid(row=5,column=0)
    fn1.grid(row=5,column=1)
    lab_mn.grid(row=7,column=0)
    mn1.grid(row=7,column=1)
    lab_ln.grid(row=9,column=0)
    ln1.grid(row=9,column=1)
    lab_ad=tk.Label(reg_page,text="Address: ")
    ad=tk.Text(reg_page,height=3,width=15)
    lab_ad.grid(row=11,column=0)
    ad.grid(row=11,column=1)
    lab_email=tk.Label(reg_page,text="Email id: ")
    email=tk.Entry(reg_page)
    lab_email.grid(row=13,column=0)
    email.grid(row=13,column=1)
    lab_phone=tk.Label(reg_page,text="Contact No.: ")
    phone=tk.Entry(reg_page)
    lab_phone.grid(row=15,column=0)
    phone.grid(row=15,column=1)
    lab_user=tk.Label(reg_page,text="User Name: ")
    us=tk.Entry(reg_page)
    lab_user.grid(row=17,column=0)
    us.grid(row=17,column=1)
    lab_pwd=tk.Label(reg_page,text="Password: ")
    lab_pwd.grid(row=19,column=0)
    pwd=tk.Entry(reg_page)
    pwd.grid(row=19,column=1)
    def sub():
        
        
        if fn1.get()=="" or mn1.get()=="" or ln1.get()=="" or ad.get("1.0","end-1c")=="" or email.get()=="" or phone.get()=="" or us.get()=="" or pwd.get()=="":
            messagebox.showinfo("Message","Please Fill all the Information")
        else:
            
            con=sqlite3.connect('final_db.db')
            cor=con.cursor()

            fname=fn1.get() 
            mname=mn1.get()
            lname=ln1.get()
            address=ad.get("1.0","end-1c")
            em=email.get()
            ph=phone.get()
            user=us.get()
            passwd=pwd.get()
            li=[(fname,mname,lname,address,em,ph,user,passwd)]
            li1=[(user,passwd)]
            cor.executemany('INSERT INTO customer_info VALUES(?,?,?,?,?,?,?,?)',li)
            messagebox.showinfo("reg","Data inserted")
            cor.executemany('INSERT INTO login VALUES(?,?)',li1)
            con.commit()
            cor.close()
            con.close()
    bt_sub=tk.Button(reg_page,text="Submit",command=sub)
    bt_sub.grid(row=21,column=6)
    def log():
        reg_page.destroy()
        top=tk.Tk()
        top.title("Login")
        lab_use=tk.Label(top,text="User Name:")
        lab_pass=tk.Label(top,text="Password:")
        tb_use=tk.Entry(top)
        tb_pass=tk.Entry(top,show='*')
        lab_dis=tk.Label(top)
        def click():
            user=tb_use.get()
            passwd=tb_pass.get()
            
            cor.execute('SELECT * FROM login WHERE user="%s" AND pass="%s"'%(user,passwd))
            if cor.fetchone() is not None:
                messagebox.showinfo("validation","welcom to our family")
                top.destroy()
                main=tk.Tk()
                main.title("Shreeji Ad Managment")
                lab1=tk.Label(main,font=('arial',40,'bold'),text="Shreeji Ad Company",bd=10,fg="blue")
                lab1.grid(row=0,column=12)
                name=tk.Label(main,text="Name:")
                name_en=tk.Entry(main)
                name.grid(row=5,column=0)
                name_en.grid(row=5,column=1)
                val= ["Ahemdabad","Junagadh","Mehsana","Rajkot"] 
                city=tk.Label(main,text="Select city:")
                cb=ttk.Combobox(main,values=val)
                city.grid(row=6,column=0)
                cb.grid(row=6,column=1)
                area=tk.Label(main,text="Select Area:")
                area.grid(row=7,column=0)
                def areaname():
                    if cb.get()=="Ahemdabad":
                        val1=["Iskon","Maninagar","Prahladnagar","Geeta mandir"]
                        cb1=ttk.Combobox(main,values=val1)
                        cb1.grid(row=7,column=1)
                    elif cb.get()=="Junagadh":
                        val1=["Timbawadi","Madhuram","Zanzarda Road","Bhavnath"]
                        cb1=ttk.Combobox(main,values=val1)
                        cb1.grid(row=7,column=1)
                    elif cb.get()=="Mehsana":
                        val1=["ONGC Circle","Modhera Circle","Radhanpur Circle"]
                        cb1=ttk.Combobox(main,values=val1)
                        cb1.grid(row=7,column=1)
                    else:
                        val1=["Ring Road","Shastri medan","Gokulnagar"]
                        cb1=ttk.Combobox(main,values=val1)
                        cb1.grid(row=7,column=1)
            
                bt=tk.Button(main,text="Click to get Area",command=areaname)
                bt.grid(row=7,column=2)
                hoarding_size=tk.Label(main,text="Select Size of Hoarding:")
                hoarding_size.grid(row=8,column=0)
                val2=["12 x 6 ft","22 x 10 ft","25 x 12 ft","40 x 12 ft","50 x 20 ft"]
                cb2=ttk.Combobox(main,values=val2)
                cb2.grid(row=8,column=1)
                day=tk.Label(main,text="Enter Days:")
                day_en=tk.Entry(main)
                day.grid(row=9,column=0)
                day_en.grid(row=9,column=1)
                pri=tk.Label(main,text="Total Amount:")
                pri_en=tk.Entry(main)
                def price():
                    if cb2.get()=="12 x 6 ft":
                        a=int(day_en.get())
                        total=a*1200
                        v=tk.StringVar()
                        v.set(str(total))
                        pri_en.config(textvariable=v)
                
                    elif cb2.get()=="22 x 10 ft":
                        a=int(day_en.get())
                        total=a*1600
                        v=tk.StringVar()
                        v.set(str(total))
                        pri_en.config(textvariable=v)
            
                    elif cb2.get()=="25 x 12 ft":
                        a=int(day_en.get())
                        total=a*2200
                        v=tk.StringVar()
                        v.set(str(total))
                        pri_en.config(textvariable=v)
            
                    elif cb2.get()=="40 x 12 ft":
                        a=int(day_en.get())
                        total=a*2500
                        v=tk.StringVar()
                        v.set(str(total))
                        pri_en.config(textvariable=v)
            
                    elif cb2.get()=="50 x 20 ft":
                        a=int(day_en.get())
                        total=a*3000
                        v=tk.StringVar()
                        v.set(str(total))
                        pri_en.config(textvariable=v)
            
            
                
                
                pri_bt=tk.Button(main,text="Click to Show Amount",command=price)
                pri.grid(row=10,column=0)
                pri_en.grid(row=10,column=1)
                pri_bt.grid(row=10,column=2)
                pro=tk.Label(main,text="Product/Company:")
                pro_en=tk.Entry(main)
                ad=tk.Label(main,text="Describe your Ad:")
                ad_box=tk.Text(main,height=3,width=15)
                pro.grid(row=11,column=0)
                pro_en.grid(row=11,column=1)
                ad.grid(row=12,column=0)
                ad_box.grid(row=12,column=1)
                em=tk.Label(main,text="Email id:")
                em_en=tk.Entry(main)
                em.grid(row=13,column=0)
                em_en.grid(row=13,column=1)
                def send_mail():
                    sender_email = "your email"
                    receiver_email = em_en.get()
                    password = "your email password"

                    message = MIMEMultipart("alternative")
                    message["Subject"] = "Thank you for using our services!!!!!"
                    message["From"] = sender_email
                    message["To"] = receiver_email

                    text = "Shreeji ad company\n hi "+name_en.get()+" your total bill price is "+pri_en.get()
                    part1 = MIMEText(text, "plain")
                    message.attach(part1)


                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message.as_string())
                        print('ok')
                fin_bt=tk.Button(main,text="Confirm order",command=send_mail)
                fin_bt.grid(row=14,column=0)
                main.mainloop()
            else:
                messagebox.showinfo("validation","Please Insert proper username & password")
        bt_new=tk.Button(top,text="New Registration",command=new_reg)
        bt=tk.Button(top,text="Login",command=click)
        lab_use.grid(row=0,column=0)
        lab_pass.grid(row=8,column=0)
        lab_dis.grid(row=22,column=0)
        tb_use.grid(row=0,column=10)
        tb_pass.grid(row=8,column=10)
        bt.grid(row=16,column=10)
        bt_new.grid(row=16,column=5)
    bt_log=tk.Button(reg_page,text="Login",command=log)
    bt_log.grid(row=21,column=3)

bt_new=tk.Button(top,text="New Registration",command=new_reg)
bt=tk.Button(top,text="Login",command=click)
lab_use.grid(row=0,column=0)
lab_pass.grid(row=8,column=0)
lab_dis.grid(row=22,column=0)
tb_use.grid(row=0,column=10)
tb_pass.grid(row=8,column=10)
bt.grid(row=16,column=10)
bt_new.grid(row=16,column=5)


top.mainloop()

