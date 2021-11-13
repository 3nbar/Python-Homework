import sqlite3

class DB:
# Ini Function ....................................................................................................................
	def __init__(self):

		with sqlite3.connect("ChamWings.db") as self.db:
			self.c=self.db.cursor()
		self.c.row_factory=sqlite3.Row
		self.c.execute("create table if not exists Client(ClientId text not null,FullName text not null,Gender text, Email text, Destination text, TripDate text, CheckInState text)")


		self.c.execute("create table if not exists Destinations(DestinationId int PRIMARY KEY , Destination text)")
		self.c.execute("create table if not exists Trips(TripId int PRIMARY KEY, DestinationId int, TripDate text , AvailableUntil text, FOREIGN KEY (DestinationId) REFERENCES Destinations (DestinationId) )")


		self.c.execute("create table if not exists Admin(AdminId int, AdminName text, AdminPassword text )")
		
# Client Functions................................................................................................................

	def insertClient(self,values):
		self.c.execute("insert into Client(ClientId ,FullName ,Gender , Email , Destination , TripDate, CheckInState ) values(?,?,?,?,?,?,?)",values)
		self.db.commit()
		return "Done"

	def checkIn(self,values):
		self.c.execute("Update Client set CheckInState='YES' where ClientId='"+values+"'")
		self.db.commit()
		return "done"

	def cancelClient(self,value):
		self.c.execute("delete from Client where ClientId = " + str(value)  )
		self.db.commit()
		return "done"

	def getcheckInState(self,value):
		data = self.c.execute("select CheckInState from Client where ClientId = " + str(value)  )
		self.db.commit()
		return data

	def editbooking(self,values):
		self.c.execute("update Client set TripDate = (?) where ClientId=(?) ",values)
		self.db.commit()
		return "done"

# Destination Functions............................................................................................................


	def insertDestinations(self,values):
		self.c.execute("insert into Destinations(DestinationId , Destination ) values(?,?)",values)
		self.db.commit()
		return "Done"

	def selectDestinations(self):
		res = self.c.execute("select Destination from Destinations" )
		data = []
		for row in res:
			for key in row:
				data.append(key)
		return data

	def selectDestinationId(self,Destination):
		res = self.c.execute("select DestinationId from Destinations where Destination='" +Destination+"'")
		for row in res:
			for key in row:
				DestinationId = key
		return DestinationId

# Trip Functions ..................................................................................................................

	def insertTrips(self,values):
		self.c.execute("insert into Trips(TripId, DestinationId, TripDate, AvailableUntil) values(?,?,?,?)",values)
		self.db.commit()
		return "Done"

	def selectTrips(self,DestinationId):
		res  = self.c.execute("select TripDate, AvailableUntil from Trips where DestinationId = " + str(DestinationId))
		TripDates = []
		TripAvDates = []
		for row in res:
			TripDates.append(row['TripDate'])
			TripAvDates.append(row['AvailableUntil'])
		return TripDates,TripAvDates

# Admin Functions ................................................................................................................


	def insertAdmin(self,values):
		self.c.execute("insert into Admin(AdminId, AdminName, AdminPassword ) values(?,?,?)",values)
		self.db.commit()
		return "Done"

	def getAdmins(self):
		data = self.c.execute("select * from Admin")
		self.db.commit()
		return data
    
# others Functions ...............................................................................................................

			
	def selectAll(self,tableName):
		res=self.c.execute("select * from " + tableName )
		self.show(res)
		

	
	def show(self,data):

		for row in data:
			for key in row:
				print(key)




db = DB()

# db.selectAll('Client')
# db.insertDestinations((0,"Damascus"))
# db.insertDestinations((1,"Lattakia"))
# db.insertDestinations((2,"Lisbon"))
# db.insertDestinations((3,"Rome"))
# db.insertDestinations((4,"London"))

# db.selectAll('Destinations')
# db.cancelFromClient(123)
# db.selectAll('Client')

# db.insertTrips(( 1,1, "22-10-2021", "20-10-2021"))
# db.insertTrips(( 2,2, "22-10-2021", "20-10-2021"))
# db.insertTrips(( 3,3, "22-10-2021", "20-10-2021"))
# db.insertTrips(( 4,4, "22-10-2021", "20-10-2021"))

# db.selectAll('Trips')

# da = db.selectDestinations()
# db.show(da)

# da = db.selectTrips((0))
# db.show(da)
# data = db.selectAll('Trips')
# db.show(data)

# db.insertAdmin((1,'haidar','59178'))
db.selectAll('Admin')
db.selectAll('Client')

