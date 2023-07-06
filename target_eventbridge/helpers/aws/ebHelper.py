import boto3
import datetime
import json

from target_eventbridge.helpers.constantsHelper import (
    AWS_EVENT_BUS_NAME,
    PAYLOAD_SOURCE_OPERTATIONS_EGENCIA,
    PAYLOAD_DETAILTYPE_OPERATIONS_EGENCIA_TRANSACTIONS
)

def sendEvent(tapData):
    client = boto3.client('events')
    data = json.dumps(tapData)
   
    time = datetime.datetime.now()
    
    entries= [
        {
            'Time': f'{time}',
            'Source': f'{PAYLOAD_SOURCE_OPERTATIONS_EGENCIA}',
            'Resources': [],
            'DetailType': f'{PAYLOAD_DETAILTYPE_OPERATIONS_EGENCIA_TRANSACTIONS}',
            'Detail': f'{data}',
            'EventBusName': f'{AWS_EVENT_BUS_NAME}',
        }
    ]

    response = client.put_events(Entries=entries)
    return response
