import Tkinter as tk
import os
import smtplib
import datetime
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class Task:
    def __init__(self):
        self.scrum = ""
        self.project = ""
        self.status = ""
        self.remark = ""
        self.bg = ""

class User:
    def __init__(self):
        with open("login.txt", "r") as fp:
            self.name = fp.readline()
            self.fromAddr = fp.readline()
            self.to = fp.readline()
            self.cc = fp.readline()
            self.pswd = fp.readline()
            fp.close()    



class SignUpUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Label(self,text="Enter your name").pack()
        self.name = tk.Entry(self)
        self.name.pack()

        tk.Label(self,text="Enter your mail address").pack()
        self.email= tk.Entry(self)
        self.email.pack()

        tk.Label(self,text="To").pack()
        self.to = tk.Entry(self)
        self.to.pack()

        tk.Label(self,text="Cc").pack()
        self.cc = tk.Entry(self)
        self.cc.pack()

        tk.Label(self,text="Enter secret mailing password").pack()
        self.password = tk.Entry(self)
        self.password.pack()

        self.button = tk.Button(self, text="Submit", command=self.saveData)
        self.button.pack()

    def saveData(self):
        with open("login.txt", "w") as fp:
            fp.write(self.name.get()+"\n")
            fp.write(self.email.get()+"\n")
            fp.write(self.to.get()+"\n")
            fp.write(self.cc.get()+"\n")
            fp.write(self.password.get())
            fp.close()
        self.quit()
        # app = MainUI()
        # app.title("ScumApp")
        # app.geometry("300x250")
        # app.mainloop()
        

class MainUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
    def a(self, tCount):
        self.taskCount = tCount
        i = self.taskCount - 1
        tk.Label(self,text="scrumCol").grid(row= 0,column=1,ipadx=5,ipady=5)
        self.scrumCol = tk.Entry(self)
        self.scrumCol.grid(row = i+1,column=1,ipadx=10,ipady=5,padx=10)

        tk.Label(self,text="PROJECT").grid(row = 0,column=2,ipadx=5,ipady=5)
        self.project = tk.Entry(self)
        self.project.grid(row = i+1,column=2,ipadx=5,ipady=5,padx=10)

        tk.Label(self,text="STATUS").grid(row = 0,column = 3,ipadx=5,ipady=5)
        self.status = tk.StringVar()
        self.status.set("ONGOING") # default value

        self.option = tk.OptionMenu(self, self.status, "ONGOING", "COMPLETED", "SCHEDULED")
        self.option.grid(row = i+1, column=3,ipadx=50,ipady=5,padx=10)

        tk.Label(self,text="REMARK").grid(row = 0,column=4,ipadx=5,ipady=5)
        self.remark = tk.Entry(self)
        self.remark.grid(row = i+1, column=4,ipadx=5,ipady=5,padx=10)
        self.controlsUI(self.taskCount)

    def controlsUI(self, i):
        self.button = tk.Button(self, text="Send", command=self.readData)
        self.button.grid(row = 2, column=1,columnspan=4,ipadx=5,ipady=5,pady=5)

        self.add = tk.Button(self, text="+", command=self.addTask)
        self.add.grid(row = 2, column = 5, ipadx = 2, ipady = 2)

    def addTask(self):
        if (self.taskCount < 3):
            self.taskCount = self.taskCount+1
            MainUI().a(self.taskCount)
            # controlsUI(self.taskCount)
        else:
            MainUI.a(self.taskCount)
            # controlsUI(self.taskCount)


    def readData(self):
        scrum1 = Task()
        scrum1.scrum = self.scrumCol.get()
        scrum1.project = self.project.get()
        scrum1.status = self.status.get()
        scrum1.remark = self.remark.get()
        self.sendMail()

    def sendMail(self):
        msg = MIMEMultipart()
        self.user = User()
        #self.time()
        self.mail = Mail()
        print(self.user.fromAddr.rstrip())
        print(self.user.pswd)
        msg['From'] = self.user.fromAddr.rstrip()
        msg['To'] = self.user.to.rstrip()
        msg['Cc'] = self.user.cc.rstrip()
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.mail.subject
        msg.attach(MIMEText(self.mail.body, 'html'))
        smtp = smtplib.SMTP("smtp.gmail.com",587)
        smtp.starttls()
        smtp.login(self.user.fromAddr.rstrip(), self.user.pswd.rstrip())
        smtp.sendmail(self.user.fromAddr.rstrip(), self.user.to.rstrip(), msg.as_string())
        smtp.close()

# def controlsUI(i):
# 	butSend = Button(top,text="SEND",command=Send,width=20)
# 	butSend.grid(row = i+2, column=1,columnspan=4,ipadx=5,ipady=5,pady=5)

# 	butAdd = Button(top,text = '+',command = lambda: [butSend.grid_forget(), butAdd.grid_forget(), addTask()], width= 1, height = 1)
# 	butAdd.grid(row = i+2, column = 5, ipadx = 2, ipady = 2)
# 	return


# def addTask():
# 	global taskCount
# 	if (taskCount < 3):
# 		taskCount = taskCount+1
# 		mainUI(taskCount)
# 		controlsUI(taskCount)
# 	else:
# 		mainUI(taskCount)
# 		controlsUI(taskCount)



class Mail(MainUI):
    def __init__(self):
        self.user = User()
        self.time = datetime.datetime.now()
        self.y = str(self.time.year)
        self.m = str(self.time.month)
        self.d = str(self.time.day)
        self.h = int(self.time.hour)
        sub = "SCRUM PLAN & REPORT_"+self.d+'/'+self.m+'/'+self.y+'_'+self.user.name
        self.subject = str(sub)
        server="smtp.gmail.com"
        
        # statusfn(status)

        self.scrum = Task()
        self.scrum.scrumCol = "SCRUM PLAN"
        self.body="""
        <table cellspacing="0" border="0">
        <colgroup width="72"></colgroup
        <colgroup width="235"></colgroup>
        <colgroup width="186"></colgroup>
        <colgroup width="106"></colgroup>
        <colgroup width="260"></colgroup>
        <tbody>
        <tr>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" height="17" align="left" bgcolor="#FF9900"><b>Sl. No.</b></td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>"""+self.scrum.scrumCol+"""</b></td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>Project</b></td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>Status</b></td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" colspan="2" valign="middle" align="center" bgcolor="#FF9900"><b>Remarks</b></td>
        </tr>
        <tr>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" height="51" align="center">1</td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center">"""+self.task.scrum+"""</td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center">"""+self.task.project+"""</td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center" bgcolor='"""+self.scrum.bg+"""'>"""+self.scrum.statusCol+"""</td>
            <td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" colspan="2" rowspan="3" valign="middle" align="center">"""+self.task.remark+"""</td>
        </tr>
        <tr>
        </tr>
        <tr>
        </tr>
        </tbody>
        </table>"""

class ScrumApp():
    initCheck = True
    def __init__(self):
        self.checkFile()
        if (self.initCheck == False):
            app = SignUpUI()
            app.title("Sign Up")
            app.geometry("00x250")
            app.mainloop()
        else:
            app = MainUI()
            app.a(1)
            app.title("ScumApp")
            app.geometry("1200x250")
            app.mainloop()

    def checkFile(self):
        try:
            os.chdir("credentials")

        except OSError:
            os.mkdir("credentials")
            os.chdir("credentials")

        try:
            flogin = open("login.txt","r")

        except IOError:
            flogin = open("login.txt","a+")
            flogin.close()
            self.initCheck = False
        finally:
            flogin.close()

ScrumApp()












def time(self):
        now = datetime.datetime.now()
        self.y = str(now.year)
        self.m = str(now.month)
        self.d = str(now.day)
        self.h = int(now.hour)
        if (self.h<10):
            plan = True
            self.scrumCol = "SCRUM PLAN"
        else:
            plan = False
            self.scrumCol = "SCRUM REPORT"