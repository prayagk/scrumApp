import os
import smtplib
import getpass
import datetime
#from email import MIMEMultipart
#from email.MIMEBase import MIMEBase
#from email.MIMEText import MIMEText
#from email.Utils import formatdate
#from email import encoders
from tkinter import *

class project {
	scrum
	projectName
	status
	remark
}

def checkFile():
	try:
		os.chdir("credentials")

	except OSError:
		os.mkdir("credentials")
		os.chdir("credentials")
		
	
	try:
		flogin = open("login.txt","r")
		
	#finally:
	#	flogin.close()
	except IOError:
		flogin = open("login.txt","a+")
		#flogin.close()
		return False
	

	
def signupUI():
	initLabelName = Label(top,text="Enter your name")
	initLabelName.grid(row=1,column=1,ipadx=5,ipady=5)
	initName = Entry(top)
	initName.grid(row=1,column=2,ipadx=5,ipady=5)
	iname = initName.get()
	
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
	
	initProceed = Button(top,text="PROCEED",command=mailverifyfn())
	initProceed.grid(row=6,column=2,ipadx=5,ipady=5)
	
	saveInfo()
	
	return
	
def saveInfo():
	pass
	

	
def mailverifyfn():
	pass


def mainUI(i=2):
	print("+")
	labelScrum=Label(top,text=scrumCol)
	labelScrum.grid(row= i,column=1,ipadx=5,ipady=5)
	butScrum = Entry(top)
	butScrum.grid(row = i+1,column=1,ipadx=10,ipady=5,padx=10)
	global scrum
	scrum = butScrum.get()

	labelProject=Label(top,text="PROJECT")
	labelProject.grid(row = i,column=2,ipadx=5,ipady=5)
	butProject = Entry(top)
	butProject.grid(row = i+1,column=2,ipadx=5,ipady=5,padx=10)
	global project
	project = butProject.get()

	statusBut = StringVar()
	statusBut.set("ONGOING") #initial value
	option = OptionMenu(top, statusBut, "  ONGOING  ", "COMPLETED", "SCHEDULED")
	option.grid(row = i+1, column=3,ipadx=50,ipady=5,padx=10)
	global status
	status = statusBut.get()

	labelRemark=Label(top,text="REMARK")
	labelRemark.grid(row = i,column=4,ipadx=5,ipady=5)
	butRemark = Text(top,width=40,height=3)
	butRemark.grid(row = i+1, column=4,ipadx=5,ipady=5,padx=10)
	global remark
	remark = butRemark.get(END)

	butSend = Button(top,text="SEND",command=Send,width=50)
	butSend.grid(row = i+2, column=1,columnspan=4,ipadx=5,ipady=5,pady=5)

	butAdd = Button(top,text = '+',command = mainUI, width= 10, height = 2)
	butAdd.grid(row = i+1, column = 5,rowspan = 2, ipadx = 10, ipady = 10)
	return





def moreProjects():
	projectCount = projectCount+1
	mainUI(projectCount)

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

def login():

	flogin = open("login.txt","a+")
	name = flogin.readline()
	send_from = flogin.readline()
	send_to = flogin.readline()
	cc = flogin.readline()
	


def Send():
	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = send_to
	msg['Cc'] = initCc
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'html'))
	smtp = smtplib.SMTP("smtp.gmail.com",587)
	smtp.starttls()	
	password="SRTTOdoo"
	smtp.login(send_from,password)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.close()
	global sent
	sent = True



	
top=Tk()
top.title("CYBRO SCRUM")
top.geometry('1200x300')

now = datetime.datetime.now()
y = str(now.year)
m = str(now.month)
d = str(now.day)
h = int(now.hour)


#start
#check for login file in credential folder
initCheck = checkFile()
ampm(h)

if initCheck==False:
	signupUI()

else:
	global projectCount
	projectCount = 0
	mainUI(0)


	login()
	name = "PRAYAG_K"
	#send_from = "minions@cybrosys.in" 
	#send_to = "minions@cybrosys.in"
	sub = "SCRUM PLAN & REPORT_"+d+'/'+m+'/'+y+'_'+name
	subject = str(sub)
	server="smtp.gmail.com"
	statusfn(status)


	body="""
	<table cellspacing="0" border="0">
	<colgroup width="72"></colgroup>
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