import os
import configparser
import sys
import json
from configparser import ConfigParser

#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.dirname(SCRIPT_DIR))
#sys.path.append(os.path.dirname(SCRIPT_DIR + "/main" ))
#sys.path.append(os.path.dirname(SCRIPT_DIR + "/main/search" ))
#sys.path.append("./" )

#print(sys.path)


import logging
logger = logging.getLogger(__name__)

OS_FILE_PATH_SEPERATOR = os.sep

base_configuration  = None

base_main_config = None

def populate_section_config ( section_type = None ) :

    if section_type == None :
        section_type = "main"

    print ( section_type )
    print ( base_configuration)

    section_type_config = dict( base_configuration.items(section_type) )

    return section_type_config


def read_file_content ( file_path ) :

    status = "failure"

    logger.info ( f"In read_file content {file_path}" )

    content = ""

    try :

        if ( os.path.isfile( file_path)  ) :

            logger.info ( f"{file_path}"  )


            with open( file_path , 'r') as f:
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

def get_config_path( input_config_dir = None , stage = None )  :

    config_file_path = None

    config_file_name = None
  
    print ( f"Input config dir : {input_config_dir}" ) 

    if input_config_dir is None : 
        config_dir = "/app/config"
    else:
        config_dir = input_config_dir

    try :

        if stage is None :
            stage = os.environ.get("STAGE", None )

        logger.info ( stage )

        if stage is None :

            config_file_name = f"config.dat"

        else :

            config_file_name = f"config.{stage}.dat"

        config_file_path = config_dir + OS_FILE_PATH_SEPERATOR + config_file_name
        logger.info ( config_file_path )
        print ( "Config File path" ) 
        print ( config_file_path ) 

    except :

        pass 

    finally :

        logger.info ( "Config"  )

        logger.info ( config_file_name )

        logger.info ( config_file_path )

        return (config_dir , config_file_path )

def read_config( input_config_dir = None , stage = None)  :

    config_dict = {}

    config_data = {}

    status = "failure"

    try :

        ( config_dir , config_file_path )  = get_config_path( input_config_dir , stage )

        logger.info ( "Config Dir"  )
        logger.info ( config_dir  )

        logger.info ( "Config Path"  )
        logger.info ( config_file_path )


        if ( os.path.isfile(config_file_path)  ) :

            logger.info ( "Config String"  )

            config_string = ""

            with open(config_file_path, 'r') as f:
                config_string = f.read()
        
            logger.info ( "Config String"  )

            logger.info ( config_string )

            print( "Config String" )
            print ( config_string )


            config = configparser.ConfigParser()

            config.optionxform = str

            config.read_string(config_string)

            logger.info ( "Config Sections" )
            logger.info ( config.sections() )

            config_main = dict( config.items("main") )

            status = "success"

            config_dict = dict ( config )

            logger.info ( "Config Successful Read" )

        else:

            logger.info ( "Config String Not Found "  )

            raise Exception ( "No Config file found. " )

    except Exception as e :

            status = "failure"

            print ( "failure " )

            print ( str ( e )  )

            logger.info ( "Exception" )

            logger.info ( str (e ) )

            config = {}


    finally :

        logger.info  (" Config" )
        logger.info ( config )

        #print ( "Config" )
        #print ( config )
    
        return ( config , status )


# Set Config based on how the program is run flask or command line 
def set_base_global_config() :

    global base_configuration
    global base_main_config

    if (  os.path.isdir ( "./config" ) ) :
        input_config_dir = "./config"
    elif ( os.path.isdir ( "/app/config") ) :
        input_config_dir = "/app/config"
    else:
        raise Exception ( "Config dir absent" )

    ( base_configuration , status  )  = read_config( input_config_dir = input_config_dir) 
    print ( "Reading Config")
    print ( base_configuration )

    base_main_config = populate_section_config ( "main")

    logger.info ( "Configuration" )
    logger.info ( "---------------------------- " )
    logger.info ( base_configuration )
    logger.info ( base_main_config )
    logger.info ( "---------------------------- " )

try :
    set_base_global_config()

except Exception as e :
    print ( str ( e ) )
    sys.exit(4)

