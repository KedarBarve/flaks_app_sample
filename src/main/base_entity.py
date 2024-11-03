import os
import sys
import json

from flask import request as flaskrequest

import json
import logging
import copy

from base_config import base_configuration 

logger = logging.getLogger(__name__)

# This is validated to be non null at startup ( server.py )

config_main = dict( base_configuration.items("main") )


class base_entity :

    # Constructor method to initialize 
    def __init__(self):

        self._key = {}

        self._key_map = {}

        self._field_map = {}

        self._data = {}

        self._collectionName = None

    @staticmethod
    def read_file_content ( file_path ) :

        status = "failure"

        logger.info ( f"In read_file content {file_path}" )

        content = ""

        try :

            tmp_file_path = file_path

            if not ( os.path.isfile( file_path)  ) :

                tmp_file_path = "./" + file_path

            with open( tmp_file_path , 'r') as f:
                content  = f.read()

            status = "success"
        
        except Exception as e :

            status = "failure"

            logger.info ( "Exception" )

            logger.info ( str (e ) )

            content = None

        finally :

            logger.info  (" Content" )
            logger.info ( content )

            return ( content , status )

    def fromFlaskRequest ( self , flaskRequest ):

        try :

            logger.info ( "Request parsing started" )

            self._key = {}

            self._data = {}

            flaskRequestJson = flaskRequest.json        

            logger.info ( "Request parsing keymap " )

            for field in self._key_map :
                if field in flaskRequestJson :
                    self._key[field] = flaskRequestJson[field]


            logger.info ( "Key is " )
            logger.info ( self._key )


            logger.info ( "Request parsing fields " )

            for field in flaskRequestJson :
                self._data[field] = flaskRequestJson[field]

            logger.info ( "Request parsing Done " )

        except Exception as e :

            logger.info ( "Invalid Request" )
            logger.info ( str (e ) )

        finally :
            logger.info ( "Out parsing " ) 


    def fromFile ( self , file_path ):

        try :

            logger.info ( "Populating  from File " )

            self._key = {}

            self._data = {}

            ( content , status ) = self.read_file_content ( file_path )

            content_dict = json.loads ( content )

            for field in self._key_map :
                if field in content_dict :
                    self._key[field] = content_dict[field]

            logger.info ( "Request parsing fields " )

            for field in content_dict :
                self._data[field] = content_dict[field]

            logger.info ( "File parsing Done " )

        except Exception as e :

            logger.info ( "Invalid Request" )
            logger.info ( str (e ) )
            print ( str(e) )

        finally :

            print ( self.getData() )
            print ( "Out file Done" )

            logger.info ( "Out File Done " ) 


    def getData(self):

        return self._data


    def getDataJson(self):

        return  json.dumps( self.getData() )


    def getCollectionName(self):

        return self._collection_name


    def getKey(self):

        return self._key

