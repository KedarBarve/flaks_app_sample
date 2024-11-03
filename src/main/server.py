from flask import Flask, jsonify
from flask import request as rq
from flask_cors import CORS

import logging
import sys

logging.basicConfig(filename='/app/logs/base_backend.log', level=logging.DEBUG)

from entities import student_url
from entities import course_url


from base_config import base_configuration

logger = logging.getLogger(__name__)

logger.info (  "Base  Config"  )
logger.info (  base_configuration  )
print (  "Base Config file" )
print (  base_configuration  )

if ( base_configuration is None ) :
    print ( "Config needs to be set properly" )
    print ( "Exiting..." )
    logger.info ( "Config needs to be set properly" )
    logger.info ( "Exiting..." )
    sys.exit(4)


app = Flask(__name__)

CORS(app)


app.register_blueprint(student_url.student_blueprint, url_prefix='/treehouse'  )

app.register_blueprint(course_url.course_blueprint, url_prefix='/treehouse'  )



logger = app.logger

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
else:
    gunicorn_app = app
