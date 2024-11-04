from flask import Blueprint
from flask import request as apiRequest
from flask import Flask, jsonify
from api_entity import api_entity
import logging
import json
import re
from . import product as treehouse_product



product_blueprint = Blueprint('product_blueprint', __name__ )

logger = logging.getLogger(__name__)


@product_blueprint.route('/helloc' ,  methods=['GET'])
def hello_product():

    try :

        data =  "Hello Product"

        return jsonify (  message = "success" , data = data ) , 200

    except Exception as e:

        exception_str = str ( e )

        return jsonify (  message = "failure" , data = exception_str  ) , 400



@product_blueprint.route('/product/<name>' ,  methods=['GET'])
def get_product(name):

    message = "failure"

    try :

        ( response , resultStatus )  = treehouse_product.get ( name = name )

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


@product_blueprint.route('/product' ,  methods=['POST'])
def post_product():

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

            ( response , resultStatus )  = treehouse_product.post ( api_entity = api_entity_detail )

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


