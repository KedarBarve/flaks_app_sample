from flask import Blueprint
from flask import request as apiRequest
from flask import Flask, jsonify
from pymongo import MongoClient
from search_entity import search_entity
import logging
import json
import re
from . import metadata as viena_metadata

import logging



metadata_search_blueprint = Blueprint('metadata_search_blueprint', __name__ )

logger = logging.getLogger(__name__)



@metadata_search_blueprint.route('/hellom' ,  methods=['GET'])
def hellom():

    try :

        data = "Hello Meta Data" 

        return jsonify (  message = "success" , data = data ) , 200


    except Exception as e:

        exception_str = str ( e )

        return jsonify (  message = "failure" , data = exception_str  ) , 400



@metadata_search_blueprint.route('/metadata' ,  methods=['GET'])
def get_metadata():

    try :

        message = "failure"

        ( response , resultStatus )  = viena_metadata.get_metadata()

        if ( resultStatus == "success" ) :
            apiStatus = 200
            message = "success"
        else:
            apiStatus = 400
            message = "failure" 

        logger.info ( response )

        return jsonify (  message = message , data = response ) , apiStatus


    except Exception as e:

        exception_str = str ( e )

        return jsonify (  message = "failure" , data = exception_str  ) , 400

