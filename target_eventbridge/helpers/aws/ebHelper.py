import boto3
from botocore.config import Config
import datetime
import json
import os

from target_eventbridge.helpers.constantsHelper import (
    AWS_EVENT_BUS_NAME,
    AWS_REGION,
    PAYLOAD_SOURCE_OPERTATIONS_EGENCIA,
    PAYLOAD_SOURCE_EMPLOYEE,
    PAYLOAD_DETAILTYPE_OPERATIONS_EGENCIA_TRANSACTIONS
)

def sendEvent(tapData):


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
            'Source': f'{PAYLOAD_SOURCE_OPERTATIONS_EGENCIA}',
            'Resources': [],
            'DetailType': f'{PAYLOAD_DETAILTYPE_OPERATIONS_EGENCIA_TRANSACTIONS}',
            'Detail': f'{data}',
            'EventBusName': f'{AWS_EVENT_BUS_NAME}',
        }
    ]

    response = client.put_events(Entries=entries)
    return response
