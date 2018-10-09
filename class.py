import os
import smtplib
import getpass
import datetime
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import encoders
from Tkinter import *
import Tkinter  as tk
def checkFile():
	try:
		os.chdir("credentials")

	except OSError:
		os.mkdir("credentials")
		os.chdir("credentials")

	try:
		flogin = open("login.txt","r")
		#print(flogin.readline())

	except IOError:
		flogin = open("login.txt","a+")
		flogin.close()
		return False
	finally:
		flogin.close()
	
initName = ""
iaddr = ""
ito = ""
icc = ""
ipswd = ""

iname = "asdasd"

class signupUI1(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title("Sign Up")

        self.label = Label(master, text="Name: ")
        self.label.pack()
		
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")
	
	# def on_button(self):
	# 	print(self.entry.get())

root = tk.Tk()
my_gui = signupUI1(root)
root.mainloop()
root.geometry('1050x400')

    


def signupUI():
	global iname
	global iaddr
	global ito
	global icc
	global ipswd

	initLabelName = Label(top,text="Enter your name")
	initLabelName.grid(row=1,column=1,ipadx=5,ipady=5)
	initName = Entry(top)
	iname = Entry.get(initName)
	initName.grid(row=1,column=2,ipadx=5,ipady=5)
	print(iname)

	initLabelAddr = Label(top,text="Enter your mail address")
	initLabelAddr.grid(row=2,column=1,ipadx=5,ipady=5)
	initAddr = Entry(top)
	initAddr.grid(row=2,column=2,ipadx=5,ipady=5)
	iaddr = initAddr.get()

	initLabelTo = Label(top,text="Enter recipient address")
	initLabelTo.grid(row=3,column=1,ipadx=5,ipady=5)
	initTo = Entry(top)
	initTo.grid(row=3,column=2,ipadx=5,ipady=5)
	ito = initTo.get()

	initLabelCc = Label(top,text="Cc")
	initLabelCc.grid(row=4,column=1,ipadx=5,ipady=5)
	initCc = Entry(top)
	initCc.grid(row=4,column=2,ipadx=5,ipady=5)
	icc = initCc.get()
	
	initLabelPswd = Label(top,text="Enter secret mailing password")
	initLabelPswd.grid(row=5,column=1,ipadx=5,ipady=5)
	initPswd = Entry(top)
	initPswd.grid(row=5,column=2,ipadx=5,ipady=5)
	ipswd = initPswd.get()
	
	initProceed = Button(top,text="PROCEED", command= lambda: saveInfo(iname))	
	initProceed.grid(row=6,column=2,ipadx=5,ipady=5)
	return
	
def saveInfo(iname):
	#global iname
	global iaddr
	global ito
	global icc
	global ipswd
	global initName
	# iname = Entry.get(initName)
	print("name : "+iname)
	flogin = open("login.txt","a+")
	flogin.write(iname)
	flogin.write(iaddr)
	flogin.write(ito)
	flogin.write(icc)
	flogin.write(ipswd)
	flogin.close()
	return

def mailverifyfn():
	pass

taskCount = 0
def mainUI(i):

	labelScrum=Label(top,text=scrumCol)
	labelScrum.grid(row= 0,column=1,ipadx=5,ipady=5)
	butScrum = Entry(top)
	butScrum.grid(row = i+1,column=1,ipadx=10,ipady=5,padx=10)
	global scrum
	scrum = butScrum.get()

	labelProject=Label(top,text="PROJECT")
	labelProject.grid(row = 0,column=2,ipadx=5,ipady=5)
	butProject = Entry(top)
	butProject.grid(row = i+1,column=2,ipadx=5,ipady=5,padx=10)
	global project
	project = butProject.get()

	labelStatus = Label(top, text = "STATUS")
	labelStatus.grid(row = 0,column = 3,ipadx=5,ipady=5)
	statusBut = StringVar()
	statusBut.set("ONGOING") #initial value
	option = OptionMenu(top, statusBut, "ONGOING", "COMPLETED", "SCHEDULED")
	option.config(width=10)
	option.grid(row = i+1, column=3,ipadx=50,ipady=5,padx=10)
	global status
	status = statusBut.get()

	labelRemark=Label(top,text="REMARK")
	labelRemark.grid(row = 0,column=4,ipadx=5,ipady=5)
	butRemark = Text(top,width=40,height=3)
	butRemark.grid(row = i+1, column=4,ipadx=5,ipady=5,padx=10)
	global remark
	remark = butRemark.get(END)
	return

def controlsUI(i):
	butSend = Button(top,text="SEND",command=Send,width=20)
	butSend.grid(row = i+2, column=1,columnspan=4,ipadx=5,ipady=5,pady=5)

	butAdd = Button(top,text = '+',command = lambda: [butSend.grid_forget(), butAdd.grid_forget(), addTask()], width= 1, height = 1)
	butAdd.grid(row = i+2, column = 5, ipadx = 2, ipady = 2)
	return

def removeControls():
	pass

def addTask():
	global taskCount
	if (taskCount < 3):
		taskCount = taskCount+1
		mainUI(taskCount)
		controlsUI(taskCount)
	else:
		mainUI(taskCount)
		controlsUI(taskCount)

def ampm(h):
        if (h<10):
                plan = True
        else:
                plan = False
        global scrumCol
        if plan:
                scrumCol = "SCRUM PLAN"
                
        else:
                scrumCol = "SCRUM REPORT"


def statusfn(status):
	global statusCol
	global bg
	global reqd
	reqd = False
	if status == "ONGOING":
		statusCol = "ONGOING"
		bg = "#FF9900"
		reqd = True
		
	elif status == "COMPLETED":
		statusCol = "COMPLETED"
		bg = "#00ff00"

	else:
		statusCol = "SCHEDULED"
		bg = "#ff0000"		


send_from=""
cc = ""
send_to = ""

def login():
	flogin = open("login.txt", "r") 
	global send_from
	global send_to
	global cc
	send_from = flogin.readline()
	send_to = flogin.readline()
	cc = flogin.readline()
	flogin.close()

def Send():
	global send_from, send_to, cc

	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = send_to
	msg['Cc'] = icc
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'html'))
	smtp = smtplib.SMTP("smtp.gmail.com",587)
	smtp.starttls()
	qqq = "prayag@cybrosys.in"
	password="prayag9633"
	smtp.login(qqq,password)
	print("from"+send_from)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.close()
	global sent
	sent = True
	
# top=tk.Tk()
# top.title("CYBRO SCRUM")
# top.geometry('1050x400')

now = datetime.datetime.now()
y = str(now.year)
m = str(now.month)
d = str(now.day)
h = int(now.hour)


#start
#check for login file in credential folder
initCheck = checkFile()
ampm(h)

if (initCheck == False):
    app = signupUI1()
    app.mainloop()
    #signupUI()

else:
	login()
	global projectCount
	projectCount = 0
	mainUI(0)
	controlsUI(0)

	name = "PRAYAG_K"
	#send_from = "minions@cybrosys.in" 
	#send_to = "minions@cybrosys.in"
	sub = "SCRUM PLAN & REPORT_"+d+'/'+m+'/'+y+'_'+name
	subject = str(sub)
	server="smtp.gmail.com"
	statusfn(status)

	body="""
	<table cellspacing="0" border="0">
	<colgroup width="72"></colgroup
	<colgroup width="235"></colgroup>
	<colgroup width="186"></colgroup>
	<colgroup width="106"></colgroup>
	<colgroup width="260"></colgroup>
	<tbody>
	  <tr>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" height="17" align="left" bgcolor="#FF9900"><b>Sl. No.</b></td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>"""+scrumCol+"""</b></td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>Project</b></td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" align="left" bgcolor="#FF9900"><b>Status</b></td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" colspan="2" valign="middle" align="center" bgcolor="#FF9900"><b>Remarks</b></td>
	  </tr>
	  <tr>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" height="51" align="center">1</td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center">"""+scrum+"""</td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center">"""+project+"""</td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" rowspan="3" valign="middle" align="center" bgcolor='"""+bg+"""'>"""+statusCol+"""</td>
		<td style="border-width: 1px; border-style: solid; border-color: rgb(0, 0, 0);" colspan="2" rowspan="3" valign="middle" align="center">"""+remark+"""</td>
	  </tr>
	  <tr>
	  </tr>
	  <tr>
	  </tr>
	</tbody>
	</table>"""

top.mainloop()