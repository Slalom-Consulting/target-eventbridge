"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink, RecordSink


from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)


class eventbridgeSink(RecordSink):

    def process_record(self, record: dict, context: dict):

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
        request = sendEvent(poc)