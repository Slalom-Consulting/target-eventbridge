"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink


from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)


class eventbridgeSink(BatchSink):

    def process_batch(self, context: dict) -> None:

        if context == {}:
            return Exception('No data Provided')
        
        else:

            poc: dict = {
                "transactions": {
                    "traveler": {
                    "name": "test-name",
                    "group": "test-group General Traveler",
                    "email": "testEmailTarget@slalom.com"
                    },
                    "line_of_business": "Airplane",
                    "point_of_sale": "USA",
                    "place_of_sale": "Gamestop"
                }
            }
            context = poc
            request = sendEvent(context)