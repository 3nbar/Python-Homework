import sqlite3

class DB:
	def __init__(self):
		self._db=sqlite3.connect("ChamWings.db")
		self._db.row_factory=sqlite3.Row
		self._db.execute("create table if not exists Client(ClientId int,FullName text,Gender int, Email text, Destination text, TripDate text)")
		self._db.execute("create table if not exists Destinations(DestinationId int, Destination text)")
		self._db.execute("create table if not exists Trips(TripId int, DestinationId int, TripDate text , AvailableUntil text )")
		self._db.execute("create table if not exists Admin(AdminId int, AdminName text, AdminPassword text )")
		self._db.commit()
		
	def insertClient(self,values):
		self._db.execute("insert into Client(ClientId ,FullName ,Gender , Email , Destination , TripDate ) values(?,?,?,?,?,?)",values)
		self._db.commit()
		return "Done"
	def cancelFromClient(self,ClientId):
		res=self._db.execute("delete from Client where ClientId=(?)", ( ClientId ) )
		return res

	def insertDestinations(self,values):
		self._db.execute("insert into Destinations(DestinationId , Destination ) values(?,?)",values)
		self._db.commit()
		return "Done"

	def insertTrips(self,values):
		self._db.execute("insert into Trips(TripId, DestinationId, TripDate, AvailableUntil) values(?,?,?,?)",values)
		self._db.commit()
		return "Done"

	def insertAdmin(self,values):
		self._db.execute("insert into Admin(AdminId, AdminName, AdminPassword ) values(?,?,?)",values)
		self._db.commit()
		return "Done"
			
	def selectAll(self,tableName):
		res=self._db.execute("select * from " + tableName )
		return res

	








