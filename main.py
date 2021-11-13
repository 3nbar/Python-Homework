import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from database import DB



db=DB()

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.widget()
        self.windowConf()
    def widget(self):
        self.frame = tk.Frame(self.master,padx=10,pady=10,  borderwidth=5,background='#669999')
        self.AdminBtn = tk.Button(self.frame, text = 'Admin', width = 25, command = self.goToLog)
        self.AdminBtn.grid(row=3,column=2,padx=10,pady=10)
        self.ClientBtn = tk.Button(self.frame, text = 'Client', width = 25, command = self.goToClient)
        self.ClientBtn.grid(row=3,column=0,padx=10,pady=10)
        self.frame.pack()

    def windowConf(self):
        self.master.title("Cham Wings")
        self.master.configure(background='#669999')

        # style=ttk.Style()
        # style.configure('TLabel',foreground='#EEEEEE', background='#669999',font=('Arial',12,'bold'))
        # style.configure('TButton',foreground='#225566',background='green',font=('Arial',12,'bold'))

        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.master.rowconfigure(3,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=1)
        self.master.columnconfigure(2,weight=1)


    def goToLog(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Log(self.newWindow)
    def goToClient(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Client(self.newWindow)
 
class Admin:
    def __init__(self, master):
        self.master = master
        self.widget()
        self.windowConf()
    def widget(self):
        self.frame = tk.Frame(self.master)

        self.ClientIdL = tk.Label( self.frame, text="Client Id",font = ('',15) ).grid(row=0,column=0,padx=10,pady=10)
        self.ClientId = tk.Entry(self.frame,bd = 5, text = "",font = ('',15))
        self.ClientId.grid(row=0,column=1,padx=10,pady=10)

        self.CancelBtn = tk.Button(self.frame, text = 'Cancel the trip', width = 25, command = self.CancelClient)
        self.CancelBtn.grid(row=2,column=0,padx=10,pady=10)

        self.frame.pack()

    def CancelClient(self):
        ClientId = self.ClientId.get()
        checkInState = db.getcheckInState(ClientId)
        for row in checkInState:
            if row['CheckInState']=='NO':
                db.cancelClient(ClientId)
                messagebox.showinfo(title='Cancel',message="the trip of the Client "+self.ClientId.get()+" is Canceled")
            else:
                messagebox.showinfo(title='Cancel',message="the trip of the Client is already checked in")

    def windowConf(self):
        self.master.title("Admin")
        self.master.configure(background='#669999')

        # style=ttk.Style()
        # style.configure('TLabel',foreground='#EEEEEE', background='#669999',font=('Arial',12,'bold'))
        # style.configure('TButton',foreground='#225566',background='green',font=('Arial',12,'bold'))

        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.master.rowconfigure(3,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=1)
        self.master.columnconfigure(2,weight=1)

class Log:
    def __init__(self, master):
        self.master = master
        self.widget()
        self.windowConf()
    def widget(self):
        self.frame = tk.Frame(self.master)

        self.AdminNameL = tk.Label( self.frame, text="AdminName",font = ('',15) ).grid(row=0,column=0,padx=10,pady=10)
        self.AdminName = tk.Entry(self.frame,bd = 5, text = "",font = ('',15))
        self.AdminName.grid(row=0,column=1,padx=10,pady=10)

        self.AdminPasswordL = tk.Label( self.frame, text="AdminPassword",bd = 5,font = ('',15) ).grid(row=1,column=0,padx=10,pady=10)
        self.AdminPassword= tk.Entry(self.frame, text = "",bd = 5,font = ('',15))
        self.AdminPassword.grid(row=1,column=1,padx=10,pady=10)

        self.LoginBtn = tk.Button(self.frame, text = 'Login', width = 25, command = self.goToAdmin)
        self.LoginBtn.grid(row=2,column=0,padx=10,pady=10)



        self.frame.pack()

    def windowConf(self):
        self.master.title("LogIn")
        self.master.configure(background='#669999')

        # style=ttk.Style()
        # style.configure('TLabel',foreground='#EEEEEE', background='#669999',font=('Arial',12,'bold'))
        # style.configure('TButton',foreground='#225566',background='green',font=('Arial',12,'bold'))

        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.master.rowconfigure(3,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=1)
        self.master.columnconfigure(2,weight=1)

    def goToAdmin(self):
        

        AdminName = self.AdminName.get()
        AdminPassword = self.AdminPassword.get()
        Admins = db.getAdmins()
        for row in Admins:
            if AdminName==row['AdminName'] :
                if AdminPassword==row['AdminPassword'] :
                    messagebox.showinfo(title='Admin Login',message="Welcome to admin :  "+AdminName+'/'+AdminPassword)
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = Admin(self.newWindow)
                else:
                    messagebox.showinfo(title='Error',message="wrong Password")
            else:
                messagebox.showinfo(title='Error',message="wrong username")

class Client:
    def __init__(self, master ):
        self.master = master
        self.widget()
        self.windowConf()

    

    def widget(self):
        self.frame = tk.Frame(self.master)

        self.ClientIdL = tk.Label( self.frame, text="ClientId",font = ('',15) ).grid(row=0,column=0,padx=10,pady=10)
        self.ClientId = tk.Entry(self.frame,bd = 5, text = "",font = ('',15))
        self.ClientId.grid(row=0,column=1,padx=10,pady=10)

        self.FullNameL = tk.Label( self.frame, text="FullName",bd = 5,font = ('',15) ).grid(row=1,column=0,padx=10,pady=10)
        self.FullName= tk.Entry(self.frame, text = "",bd = 5,font = ('',15))
        self.FullName.grid(row=1,column=1,padx=10,pady=10)

        self.GenderL = tk.Label( self.frame, text="Gender",bd = 5,font = ('',15) ).grid(row=2,column=0,padx=10)
        self.Gender=StringVar()
        self.Gender.set('Male')
        
        tk.Radiobutton(self.frame,text='Male',variable=self.Gender, value="Male").grid(row=2,column=1)
        tk.Radiobutton(self.frame,text='Female',variable=self.Gender, value="Female").grid(row=2,column=2,padx=10,pady=10)

        self.EmailL = tk.Label( self.frame, text="Email",bd = 5,font = ('',15) ).grid(row=3,column=0,padx=10,pady=10)
        self.Email= tk.Entry(self.frame, text = "",bd = 5,font = ('',15))
        self.Email.grid(row=3,column=1,padx=10,pady=10)


        
        Destinations = db.selectDestinations()
        # print(data)

        # Destinations = ['Bahamas','Canada', 'Cuba','United States']
        self.Destination = StringVar()
        self.Destination.set(Destinations[3])
        
        self.DestinationL = tk.Label( self.frame, text="Destination",bd = 5,font = ('',15) ).grid(row=4,column=0,padx=10,pady=10)
        self.DestinationList= tk.OptionMenu(self.frame, self.Destination ,*Destinations, command =self.getDate)
        self.DestinationList.grid(row=4,column=1,padx=10,pady=10)

        # self.TripDates = ['2020','2020', '2020','2021']

        # self.TripAvDates = ['2020','2020', '2020','2021']


        
        self.SubmitBtn = tk.Button(self.frame, text = 'Submit', width = 25, command = self.insertClient)
        self.SubmitBtn.grid(row=6,column=1,padx=10,pady=10)
        
        self.ClientCancelBtn = tk.Button(self.frame, text = 'Cancel the trip by Id ', width = 25, command = self.cancelClient)
        self.ClientCancelBtn.grid(row=6,column=2,padx=10,pady=10)

        self.ClientcheckInBtn = tk.Button(self.frame, text = 'Check in ', width = 25, command = self.ClientcheckIn)
        self.ClientcheckInBtn.grid(row=6,column=0,padx=10,pady=10)

        self.frame.pack()
    def insertClient(self):
        ClientId = self.ClientId.get()
        FullName = self.FullName.get()
        Gender = self.Gender.get()
        Email = self.Email.get()
        Destination = self.Destination.get()
        TripDate = self.TripDate.get()
        CheckInState = 'NO'
        values = [ClientId ,FullName ,Gender , Email , Destination , TripDate, CheckInState ]
        db.insertClient(values)
        db.selectAll('Client')

    

        messagebox.showinfo(title='Add Client',message="Data inserted"+self.ClientId.get()+'/'+FullName+'/'+Gender+'/'+Email+'/'+Destination+'/'+TripDate)
    def cancelClient(self):
        ClientId = self.ClientId.get()
        db.cancelClient(ClientId)
        messagebox.showinfo(title='Cancel  the trip',message="the trip is Canceld of the client"+self.ClientId.get())

    def ClientcheckIn(self):
        ClientId = self.ClientId.get()
        db.checkIn(ClientId)
        messagebox.showinfo(title='check in',message="the trip is checked in of the client "+self.ClientId.get())
        db.selectAll('Client')

    def getDate(self,event):
        destination = self.Destination.get()
        destinationId = db.selectDestinationId(destination)

        TripDates,TripAvDates = db.selectTrips(destinationId)
        # print(TripDates)
        # print(TripAvDates)
        self.TripDates = TripDates
        self.TripAvDates = TripAvDates
        self.TripDate = StringVar()
        self.TripDate.set(self.TripDates[0])

        self.TripDateL = tk.Label( self.frame, text="Trip Date/availability",bd = 5,font = ('',15) ).grid(row=5,column=0,padx=10,pady=10)
        self.TripDateList= tk.OptionMenu(self.frame, self.TripDate,*self.TripDates)
        self.TripDateList.grid(row=5,column=1,padx=10,pady=10)

        
        self.TripAvDate = StringVar()
        self.TripAvDate.set(self.TripAvDates[0])

        self.TripDateAvList= tk.OptionMenu(self.frame, self.TripAvDate,*self.TripAvDates)
        self.TripDateAvList.grid(row=5,column=2,padx=10,pady=10)
        # print('hi')


    def windowConf(self):
        self.master.title("Client")
        self.master.configure(background='#669999')

        # style=ttk.Style()
        # style.configure('TLabel',foreground='#EEEEEE', background='#669999',font=('Arial',12,'bold'))
        # style.configure('TButton',foreground='#225566',background='green',font=('Arial',12,'bold'))

        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.master.rowconfigure(3,weight=1)
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=1)
        self.master.columnconfigure(2,weight=1)
    
def main(): 
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()