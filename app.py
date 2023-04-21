#-*- coding: utf-8 -*-
__author__ = "Chirag Rathod (Srce Cde)"
__license__ = "MIT"
__email__ = "chiragr83@gmail.com"
__maintainer__ = "Chirag Rathod (Srce Cde)"

import json
import requests

def handler(event, context):

    # TODO implementation
    
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 300,
        'body': json.dumps({"message": "Lambda Container image invoked By codeBuild!",
                            "event": event})
    }