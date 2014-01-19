from Crypto import Random
from google.appengine.ext import db

class Cloud(db.Model):
	secretKey = db.ByteStringProperty(required=True)
	IV = db.ByteStringProperty(required=True)
		
	def getSecretKey(self):
		return self.secretKey
			
	def getIV(self):
		return self.IV

	def changeSecretKey(self,secretKey=None):
		if len(secretKey) != 32:
			return False

		if not secretKey:
			secretKey = Random.new().read(32)
		
		self.secretKey = secretKey
		self.IV = Random.new().read(16)
		self.put()
		return True

def getCloud():
	q = db.Query(Cloud)
	c = q.get()
	if not c:
		c = Cloud(secretKey = Random.new().read(32),
				  IV = Random.new().read(16))
		c.put()
	return c