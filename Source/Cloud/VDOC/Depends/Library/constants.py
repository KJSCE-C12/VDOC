##############################
##########Constants###########
##############################
C_ALLOWED_USERNAME_LENGTH = 6
C_ALLOWED_PASSWORD_LENGTH = 6
C_ALLOWED_IMAGE_COUNT = 1

##############################
##########Error Codes#########
##############################

######### USER ERRORS #########
#-----------------------------#

########## Login ##########
ERROR_USER_LOGIN_USERNAME_DOES_NOT_EXIST = 0
ERROR_USER_LOGIN_INCORRECT_PASSWORD = 1
ERROR_USER_LOGIN_USERNAME_LENGTH_TOO_SMALL = 2
ERROR_USER_LOGIN_PASSWORD_LENGTH_TOO_SMALL = 3

########## Register ##########
ERROR_USER_REGISTER_USERNAME_EXISTS = 20
ERROR_USER_REGISTER_INVALID_GENDER = 21

########## Token ##########
ERROR_USER_REFRESH_TOKEN_INVALID = 40
ERROR_USER_ACCESS_TOKEN_INVALID = 41

########## General ##########
ERROR_GENERAL_PARAMETER_ABSENT = 50

########## Server ##########
ERROR_SERVER_ALL_SERVERS_ALLOCATED = 200

########## Cloudlet ##########
ERRROR_CLOUDLET_SERVER_ALLOCATION_NOT_POSSIBLE = 300
ERRROR_CLOUDLET_SERVER_NO_SUCH_NAME = 301