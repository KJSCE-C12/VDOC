from ...Library import constants
from google.appengine.ext import db

from ApplicationServer import ApplicationServer

class UserDisk(db.Model):
	currentLocation = db.ReferenceProperty(ApplicationServer,required=True);
	locations = db.ListProperty(db.Key)
	
	def addLocation(self, location):
		self.locations.append(location)
	#Disk Image elimination logic
		if len(self.locations) > constants.C_ALLOWED_IMAGE_COUNT:
			self.locations[0].deleteDiskImage(self.key())
			self.locations.pop(0)
		self.update()

	def update(self):
		self.put()
	
	@classmethod
	def createImage(cls,currentLocation):
		ud = UserDisk(currentLocation = currentLocation)
		ud.locations = [currentLocation.key()]
		ud.put()
		return ud
		