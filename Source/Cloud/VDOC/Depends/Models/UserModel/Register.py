from .. import *
from ...Library import *

from google.appengine.ext import db

def createUser(username,password,gender,preferredCloudletServer=None):
    
    #Work out preferred cloudlet server information
    
    u = User(username = username,
             password = password,
             gender = gender)
    if not u.validateAndStore():
        return response.makeError(constants.ERROR_USER_REGISTER_USERNAME_EXISTS, description="Username already exists")

    #Make Access token and allocation requirements
    return response.makeResponse({'status':100,'description':'Account Created'})