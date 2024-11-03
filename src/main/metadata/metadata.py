from pymongo import MongoClient
import logging


if __name__ != '__main__' :
    from egsc_torus_config import  egsc_torus_metadata_config
else:
    from ..egsc_torus_config import  egsc_torus_metadata_config


logger = logging.getLogger(__name__)

def get_metadata() :

    resultStatus = "success"

    try :

        return ( egsc_torus_metadata_config , resultStatus )

    except Exception as e:
    
        resultStatus = "failure"

        exception_str = str ( e )

        return ( {} , resultStatus )


if __name__ == '__main__':


    ( response, status ) =  get_metadata ()

    print ( response )

