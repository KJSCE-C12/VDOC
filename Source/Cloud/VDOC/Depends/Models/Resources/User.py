from google.appengine.ext import db

from UserDisk import UserDisk

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    gender = db.StringProperty(required=True, choices=set(["male","female","other"]))
    diskImage = db.ReferenceProperty(UserDisk)
	
    def validateAndStore(self):
        q = db.Query(User)
        q.filter("username =", self.username)
        if q.count() > 0:
            print "Put not unique for {0} (User)".format(self.username)
            return False
        
        self.put()
        return True
        
    def addDiskImage(self, diskImage):
    	self.diskImage = diskImage
    	self.update()
    	
    def update(self):
    	self.put()
    
    @classmethod
    def getUserByUsername(cls, username):
		q = db.Query(User).filter("username =",username)
		return q.get()