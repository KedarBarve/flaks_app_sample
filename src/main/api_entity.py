from base_entity import base_entity
from base_config import  base_configuration

import logging


logger = logging.getLogger(__name__)


class api_entity ( base_entity ) :

    # Constructor method 

    def __init__(self, name = None , collection_name = None  ):

        super().__init__()

        self._collection_name = ""

        self._key_map = {}
        
        self.name = name

        self._data = {}

        self._data["name"] = self.name

        logger.info ( "Created object" )



    def fromFlaskRequest ( self , flaskRequest ):

        super( api_entity , self ). fromFlaskRequest (  flaskRequest )

        logger.info ( "Created object from flaskRequest" )


    def getRequestFieldData ( self , field_name ):

        return  self._data.get ( field_name , None )


    def validateInputRequest( self  ) :

        logger.info ( "Started Basic Validation" )

        return ( True , "Validations Successful" )


if __name__ == '__main__':

    r1 = api_entity ( name = "dummy" )



