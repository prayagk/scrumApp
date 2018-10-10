import Tkinter as tk
import os
import datetime


class Scrum:
    def __init__(self):
        self.scrum = ""
        self.project = ""
        self.status = ""
        self.remark = ""        

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
            fp.write(self.password.get())
            fp.close()
        self.quit()
        # app = MainUI()
        # app.title("ScumApp")
        # app.geometry("300x250")
        # app.mainloop()
        


class MainUI(tk.Tk, Scrum):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Label(self,text="scrumCol").pack()
        self.scrum = tk.Entry(self)
        self.scrum.pack()

        tk.Label(self,text="PROJECT").pack()
        self.project = tk.Entry(self)
        self.project.pack()

        tk.Label(self,text="STATUS").pack()
        self.status = tk.StringVar()
        self.status.set("ONGOING") # default value

        self.option = tk.OptionMenu(self, self.status, "ONGOING", "COMPLETED", "SCHEDULED")
        self.option.pack()

        tk.Label(self,text="REMARK").pack()
        self.remark = tk.Entry(self)
        self.remark.pack()

        self.button = tk.Button(self, text="Send", command=self.readData)
        self.button.pack()

    def readData(self):
        scrum1 = Scrum()
        scrum1.scrum = self.scrum.get()
        scrum1.project = self.project.get()
        scrum1.status = self.status.get()
        scrum1.remark = self.remark.get()

    def time(self):
        now = datetime.datetime.now()
        y = str(now.year)
        m = str(now.month)
        d = str(now.day)
        h = int(now.hour)
        if (h<10):
            plan = True
            scrumCol = "SCRUM PLAN"
        else:
            plan = False
            scrumCol = "SCRUM REPORT"                

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



class ScrumApp():
    initCheck = True
    def __init__(self):
        self.checkFile()
        if (self.initCheck == False):
            app = SignUpUI()
            app.title("Sign Up")
            app.geometry("300x250")
            app.mainloop()
        else:
            app = MainUI()
            app.title("ScumApp")
            app.geometry("300x250")
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

class Mail:
    def __init__(self):

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

ScrumApp()