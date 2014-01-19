from google.appengine.ext import db

from ApplicationServer import ApplicationServer

class CloudletServer(db.Model):
	DomainName = db.StringProperty(required=True)
	IPAddress = db.StringProperty(required=True)
	secretKey = db.ByteStringProperty(required=True)
	serverIV = db.ByteStringProperty(required=True)
	
	def getApplicationServers(self):
		lst = []
		q =db.Query(ApplicationServer).filter("parentCloudlet =",self.key())
		for p in q.run():
			lst.append(p)
		return lst
	
	def getBestApplicationServerCandidate(self):
		#TODO: Better Algorithm
		return self.getApplicationServers()[0]
	
	def getDiskImageFromCloudlet(self, cloudletServer):
		#TODO: Command Cloudlet to shift disk image
		print "Empty Method"
	
	def validateAndStore(self):
		q = db.Query(CloudletServer)
		q.filter("IPAddress =", self.IPAddress)
		if q.count() != 0:
			return False	
		self.put()
		return True
	
	@classmethod
	def createCloudlet(cls,DomainName, IPAddress, secretKey, serverIV):
		cloudlet = CloudletServer(DomainName=DomainName, IPAddress=IPAddress,secretKey=secretKey,serverIV=serverIV)
		print 'Hello {0}'.format(cloudlet.DomainName)
		if not cloudlet.validateAndStore():
			return None
		return cloudlet
	
	@classmethod
	def getCloudletServerByDomainName(cls,name):
		return db.Query(CloudletServer).filter("DomainName =",name).get()
	
	@classmethod
	def getBestCloudletServerCandidate(cls):
		#TODO: Better Algorithm
		return db.Query(CloudletServer).get()
	
	@classmethod
	def isAllocationPossible(cls,cloudletServer):
		return True
	
	@classmethod
	def shiftDiskImageToCloudletServer(cls,diskImage, cloudletServer):
		cloudletServer.getDiskImageFromCloudlet(diskImage.locations[0])
		diskImage.addLocation(cloudletServer)
		return True