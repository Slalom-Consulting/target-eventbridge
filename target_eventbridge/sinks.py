"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink, RecordSink

from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)

from target_eventbridge.helpers.schemas.sampleRecord import (
    sample_record
)

class eventbridgeSink(RecordSink):

    def process_record(self, record: dict, context: dict):
        
        event_bus_name = self.config["event_bus_name"]
        event_detail_type = self.config["event_detail_type"]
        event_source = self.config["event_source"]

        request = sendEvent(event_bus_name, event_detail_type, event_source, sample_record)