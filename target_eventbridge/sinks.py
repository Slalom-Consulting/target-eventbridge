"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink

from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)

class eventbridgeSink(BatchSink):
    def write_to_file(self, file_path, data):
        try:
            with open(file_path, "w") as file:
                file.write(data)
            print("Data written to file successfully.")
        except IOError:
            print(f"Error writing to file: {file_path}")


    def process_batch(self, context: dict) -> None:
        # Batch process the records received from the Tap

        event_bus_name = self.config["event_bus_name"]
        event_detail_type = self.config["event_detail_type"]
        event_source = self.config["event_source"]

        # # NOTE it is possible to transform data in this step prior to uploading to eventbridge. 
        # for single_record in context["records"]:
        #     # traveler = single_record["traveler"]
        #     # transformed_record = {
        #     #     "traveler": f'{traveler}'
        #     # }
        #     record_list.append(transformed_record) or self.records.appends(transformed_record)

        result = sendEvent(event_bus_name, event_detail_type, event_source, context["records"])
        result_output = str(result)
        self.write_to_file('requestResponse.json', result_output)

        
        