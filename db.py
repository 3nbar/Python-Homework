import sqlite3

class DB:
	def __init__(self):

		with sqlite3.connect("ChamWings.db") as self.db:
			self.c=self.db.cursor()
		self.c.row_factory=sqlite3.Row
		self.c.execute("create table if not exists Client(ClientId int,FullName text,Gender int, Email text, Destination text, TripDate text)")
		self.c.execute("create table if not exists Destinations(DestinationId int, Destination text)")
		self.c.execute("create table if not exists Trips(TripId int, DestinationId int, TripDate text , AvailableUntil text )")
		self.c.execute("create table if not exists Admin(AdminId int, AdminName text, AdminPassword text )")
		
		
	def insertClient(self,values):
		self.c.execute("insert into Client(ClientId ,FullName ,Gender , Email , Destination , TripDate ) values(?,?,?,?,?,?)",values)
		self.db.commit()
		return "Done"
	def cancelFromClient(self,ClientId):
		res=self.c.execute("delete from Client where ClientId=(?)", ( ClientId ) )
		return res

	def insertDestinations(self,values):
		self.c.execute("insert into Destinations(DestinationId , Destination ) values(?,?)",values)
		self.db.commit()
		return "Done"

	def insertTrips(self,values):
		self.c.execute("insert into Trips(TripId, DestinationId, TripDate, AvailableUntil) values(?,?,?,?)",values)
		self.db.commit()
		return "Done"

	def insertAdmin(self,values):
		self.c.execute("insert into Admin(AdminId, AdminName, AdminPassword ) values(?,?,?)",values)
		self.db.commit()
		return "Done"
			
	def selectAll(self,tableName):
		res=self.c.execute("select * from " + tableName )
		return res

	





db = DB()
db.insertDestinations((1,'Rome'))
data = db.selectAll("Destinations")
for row in data:
	print("DestinationId : {} Destination : {}".format(row["DestinationId"],row["Destination"]))