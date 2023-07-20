import boto3
from botocore.config import Config
import json

from target_eventbridge.helpers.constantsHelper import (
    AWS_REGION,
)

def sendEvent(event_bus_name, event_detail_type, event_source, tapRecords):

    if tapRecords == []:
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

    events = []

    for single_record in tapRecords:
        json_record = json.dumps(single_record)

        single_event = {
            'Source': f'{event_source}',
            'DetailType': f'{event_detail_type}',
            'Detail': json_record,
            'EventBusName': f'{event_bus_name}',
            }
        
        events.append(single_event)
    
    batch_size = 10
    total_events = len(events)

    for start_index in range(0, total_events, batch_size):
        end_index = start_index + batch_size
        batch = events[start_index:end_index]

        client.put_events(Entries=batch)

