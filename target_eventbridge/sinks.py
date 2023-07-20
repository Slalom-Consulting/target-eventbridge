"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink

from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)

class eventbridgeSink(BatchSink):

    def process_batch(self, context: dict) -> None:
        # Batch process the records received from the Tap

        event_bus_name = self.config["event_bus_name"]
        event_detail_type = self.config["event_detail_type"]
        event_source = self.config["event_source"]

        sendEvent(event_bus_name, event_detail_type, event_source, context["records"])


        
        