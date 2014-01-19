from Depends.Models.UserModel import *
from Depends.Library import *
from Depends.Models.Security import *
import webapp2

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        #Check for username and password being set:
        username = self.request.get('username');
        password = self.request.get('password');
        preferredServer = self.request.get('cloudlet');
		
        if len(username)<constants.C_ALLOWED_USERNAME_LENGTH:
            self.response.write(response.makeError(constants.ERROR_USER_LOGIN_USERNAME_LENGTH_TOO_SMALL, description="Username length too small"))
            return;
        
        if len(password)<constants.C_ALLOWED_PASSWORD_LENGTH:
            self.response.write(response.makeError(constants.ERROR_USER_LOGIN_PASSWORD_LENGTH_TOO_SMALL, description="Password length too small"))
            return;
        
        self.response.write(Login.userLogin(username,password,preferredServer))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        #Check for username and password being set:
        username = self.request.get('username');
        password = self.request.get('password');
        gender = self.request.get('gender');
        
        if len(username)<constants.C_ALLOWED_USERNAME_LENGTH:
            self.response.write(response.makeError(constants.ERROR_USER_LOGIN_USERNAME_LENGTH_TOO_SMALL, description="Username length too small"))
            return;
        
        if len(password)<constants.C_ALLOWED_PASSWORD_LENGTH:
            self.response.write(response.makeError(constants.ERROR_USER_LOGIN_PASSWORD_LENGTH_TOO_SMALL, description="Password length too small"))
            return;

        if gender!="male" and gender!="female" and gender!="other":
            self.response.write(response.makeError(constants.ERROR_USER_REGISTER_INVALID_GENDER, description="Gender selection invalid, possible values: male, female, other"))
            return

        self.response.write(Register.createUser(username,password,gender))

class AccessTokenHandler(webapp2.RequestHandler):
	def get(self):
		refreshToken = self.request.get('refreshToken');
		if len(refreshToken) == 0:
			self.response.write(response.makeError(constants.ERROR_GENERAL_PARAMETER_ABSENT,"Refresh Token not specified"))
			return

		self.response.write(AccessToken.getAccessToken(refreshToken))

class DefaultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Incorrect Usage')

app = webapp2.WSGIApplication([
                               ('/user/login', LoginHandler),
                               ('/user/create', CreateHandler),
							   ('/user/access_token', AccessTokenHandler),
                               ('/user', DefaultHandler)
                               ], debug=True)