import boto3
from botocore.config import Config
import datetime
import json
import os

from target_eventbridge.helpers.constantsHelper import (
    AWS_REGION,
)

def sendEvent(event_bus_name, event_detail_type, event_source, tapData):

    if tapData == {}:
        raise Exception('No data returned from tap')

    
    config = Config(
        region_name = f'{AWS_REGION}',
        signature_version = 'v4',
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
    client = boto3.client('events', config=config)


    data = json.dumps(tapData)
    time = datetime.datetime.now()
    entries= [
        {
            'Time': f'{time}',
            'Source': f'{event_source}',
            'Resources': [],
            'DetailType': f'{event_detail_type}',
            'Detail': f'{data}',
            'EventBusName': f'{event_bus_name}',
        }
    ]

    response = client.put_events(Entries=entries)
    return response
