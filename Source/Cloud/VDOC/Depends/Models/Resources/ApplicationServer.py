from google.appengine.ext import db

class ApplicationServer(db.Model):
	parentCloudlet = db.ReferenceProperty(required=True)
	port = db.IntegerProperty(required=True)
	
	
	def deleteDiskImage(self, diskImage):
	#TODO: Tell parent cloud to tell application server to delete the disk image
		print "Empty Method deleteDiskImage"
	
	def validateAndStore(self):
		q = db.Query(ApplicationServer)
		q.filter("parentCloudlet =", self.parentCloudlet).filter("port = ",self.port)
		if not q.count() == 0:
			return False
		
		self.put()
		return True

	@classmethod
	def createApplicationServer(cls,parentCloudlet,port):
		a = ApplicationServer(parentCloudlet=parentCloudlet,port=port)
		
		if not a.validateAndStore():
			return None
		
		return a