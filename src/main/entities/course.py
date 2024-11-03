import logging
import sys


if __name__ != '__main__' :
    from base_config import  base_configuration
else:
    from ..base_config import  base_configuration

from api_entity import api_entity

logger = logging.getLogger(__name__)

course_data = {}


def get ( name ) :

    data = {}

    global course_data

    try :

        if name in course_data :
            data =  course_data[name]
        else:
            data =  "Not found"

        results_response = data

        returnStatus = "success" 

    except Exception as e:

        exception_str =  str ( e )

        results_response = { "error" : exception_str  }

        returnStatus = "failure" 

    finally :

        return ( results_response , returnStatus )


def post( api_entity = None ) :


    global course_data

    exception_str = ""

    results_response = { "error" : exception_str  }

    try :
    
        if api_entity :
            name = api_entity.getRequestFieldData( "name" )

        course_data[name] = api_entity.getData()

        results_response = { "data" : course_data[name]  }

        returnStatus = "success"

    except Exception as e:

        exception_str =  str ( e )

        results_response = { "error" : exception_str  }

        returnStatus = "failure" 

    finally :

        return ( results_response , returnStatus )

if __name__ == '__main__':

    api_entity_detail = api_entity()

    input_file_path  = sys.argv[1] 

    api_entity_detail.fromFile( input_file_path )

    if api_entity :
        search_phrase = api_entity_detail.getRequestFieldData( "search_phrase" )
        print ( search_phrase )
   
    ( response, status ) =  search( api_entity = api_entity_detail )

    print ( response )

