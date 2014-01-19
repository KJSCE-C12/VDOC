from ..Security import *
from ..Resources import *
from ...Library import *

from google.appengine.ext import db

def userLogin(username,password,preferredCloudletServer=None):
	u = User.getUserByUsername(username)
	
	if not u:
		return response.makeError(constants.ERROR_USER_LOGIN_USERNAME_DOES_NOT_EXIST, description="Invalid username")
	
	if u.password != password:
		return response.makeError(constants.ERROR_USER_LOGIN_INCORRECT_PASSWORD, description="Password invalid")
	
	if not preferredCloudletServer:
		preferredCloudletServer = CloudletServer.getBestCloudletServerCandidate()
		if not preferredCloudletServer:
			return response.makeError(constants.ERROR_SERVER_ALL_SERVERS_ALLOCATED, description="All servers have been allocated")
	else:
		preferredCloudletServer = CloudletServer.getCloudletServerByDomainName(preferredCloudletServer)
		if not preferredCloudletServer:
			return response.makeError(constants.ERRROR_CLOUDLET_SERVER_NO_SUCH_NAME, description="Cloudlet server does not exist")
		if not CloudletServer.isAllocationPossible(preferredCloudletServer):
			return response.makeError(constants.ERRROR_CLOUDLET_SERVER_ALLOCATION_NOT_POSSIBLE, description="Allocation in cloudlet server not possible")

	#Check if user has a disk image created
	if not u.diskImage:
	#Allocate a diskImage
		appServer = preferredCloudletServer.getBestApplicationServerCandidate()
		u.addDiskImage(UserDisk.createImage(appServer))
		#TODO: Command Application Server to create a disk Image
	else:
	#Check if disk image resides in the cloudlet server
		if not any(any(location==tServer.key() for location in u.diskImage.locations) for tServer in preferredCloudletServer.getApplicationServers()):
			print "Disk Image not found in cloudlet server"
			CloudletServer.shiftDiskImageToCloudletServer(u.diskImage,preferredCloudletServer)
	
	return response.makeResponse({'refreshToken':Crypt.getRefreshToken(username,password), 'cloudlet_name': preferredCloudletServer.DomainName})