from ..Security import *
from ..Resources import *
from ...Library import *

def getAccessToken(refreshToken, preferredServerName=None):
	#Decode and validate refreshToken
	credentials = Crypt.getUsernameAndPasswordFromToken(refreshToken)
	if not credentials:
		return response.makeError(constants.ERROR_USER_REFRESH_TOKEN_INVALID, "Invalid Refresh token")
	
	u = User.getUserByUsername(credentials['username'])
	
	#Lookup server information and check if server exists
	if not preferredServerName:
		preferredServerName = CloudletServer.getBestCloudletServerCandidate()
	else:
	#Check if allocation is possible
		preferredServer = CloudletServer.getCloudletServerByDomainName(preferredServerName)
		if not preferredServer:
			return response.makeError(constants.ERRROR_CLOUDLET_SERVER_NO_SUCH_NAME, description="Cloudlet server does not exist")
		if not CloudletServer.isAllocationPossible(preferredServer):
			return response.makeError(constants.ERRROR_CLOUDLET_SERVER_ALLOCATION_NOT_POSSIBLE, description="Allocation in cloudlet server not possible")
	
	
	#Check if user has a disk image created
	if not u.diskImage:
		#Allocate a diskImage
		print 'Disk Image had not been created'
		appServer = preferredServer.getBestApplicationServerCandidate()
		u.addDiskImage(UserDisk.createImage(appServer))
	#TODO: Command Application Server to create a disk Image
	else:
	#Check if disk image resides in the cloudlet server
		if not any(any(location==tServer.key() for location in u.diskImage.locations) for tServer in preferredServer.getApplicationServers()):
			print "Disk Image not found in cloudlet server"
			CloudletServer.shiftDiskImageToCloudletServer(u.diskImage,preferredServer)

	#Get server key and return access token
	return response.makeResponse({'accessToken':
								Crypt.getAccessToken(
										credentials['username'],
										credentials['password'],
										preferredServer.secretKey, 
										preferredServer.serverIV),
									'IPAddress': preferredServer.IPAddress})