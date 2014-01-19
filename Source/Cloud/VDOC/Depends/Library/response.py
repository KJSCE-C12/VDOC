import json

REPONSE_MODULE_ALLOW_DESCRIPTION = True

def makeError(code,description=None):
    if not description or not REPONSE_MODULE_ALLOW_DESCRIPTION:
        return json.dumps({'response_type':'error',
                'body':{
                    'code':code,
                    }
                })
    else:
        return json.dumps({'response_type':'error',
                'body':{
                    'code':code,
                    'description':description
                    }
                })

def makeResponse(body):
    return json.dumps({'response_type':'response','body':body})