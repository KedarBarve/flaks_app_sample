from flask import Blueprint
from flask import request as apiRequest
from flask import Flask, jsonify
from api_entity import api_entity
import logging
import json
import re
from . import customer as treehouse_customer

import logging



customer_blueprint = Blueprint('customer_blueprint', __name__ )

logger = logging.getLogger(__name__)

@customer_blueprint.route('/hellos' ,  methods=['GET'])
def hello_customer():

    try :

        data = "Hello Customer" 

        return jsonify (  message = "success" , data = data ) , 200


    except Exception as e:

        exception_str = str ( e )

        return jsonify (  message = "failure" , data = exception_str  ) , 400



@customer_blueprint.route('/customer/<name>' ,  methods=['GET'])
def get_customer(name):

    try :

        message = "failure"

        ( response , resultStatus )  = treehouse_customer.get ( name = name )

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


@customer_blueprint.route('/customer' ,  methods=['POST'])
def post_customer():

    validRequest = False 

    logger.info ( "In hello1" )

    validationMessage  =  "Validation Error"

    try :

        api_entity_detail = api_entity()

        logger.info ( "In hello2" )

        api_entity_detail.fromFlaskRequest( apiRequest )

        logger.info ( "Parsed Request" )

        logger.info ( "Validating Request" )

        ( validRequest,validationMessage )  =  api_entity_detail.validateInputRequest()

        logger.info ( "Validated Request" )

        logger.info ( str(validRequest) + " " + str ( validationMessage )  )

        logger.info ( api_entity_detail.getData() )


        if validRequest :

            ( response , resultStatus )  = treehouse_customer.post ( api_entity = api_entity_detail )

            if ( resultStatus == "success" ) :
                apiStatus = 200
                message = "success"
            else:
                apiStatus = 400
                message = "failure" 


        else:

            raise Exception ( validationMessage )

        return jsonify (  message = message , data = response ) , apiStatus

    except Exception as e :

        exception_str = str ( e )

        return jsonify (  message = "failure" , data = exception_str  ) , 400

