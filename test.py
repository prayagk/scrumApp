import Tkinter as tk
import os

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


class MainUI(tk.Tk):
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
        self.status.set("one") # default value

        self.option = tk.OptionMenu(self, self.status, "ONGOING", "COMPLETED", "SCHEDULED")
        self.option.pack()


        statusBut.set("ONGOING") #initial value
        option = OptionMenu(top, statusBut, "ONGOING", "COMPLETED", "SCHEDULED")
        option.config(width=10)
        option.grid(row = i+1, column=3,ipadx=50,ipady=5,padx=10)
        global status
        status = statusBut.get()


        # labelRemark=Label(top,text="REMARK")
        # labelRemark.grid(row = 0,column=4,ipadx=5,ipady=5)
        # butRemark = Text(top,width=40,height=3)
        # butRemark.grid(row = i+1, column=4,ipadx=5,ipady=5,padx=10)
        # global remark
        # remark = butRemark.get(END)
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

ScrumApp()