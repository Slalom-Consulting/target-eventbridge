"""eventbridge target sink class, which handles writing streams."""

from __future__ import annotations

from singer_sdk.sinks import BatchSink


from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)


class eventbridgeSink(BatchSink):
    """eventbridge target sink class."""


    def start_batch(self, context: dict) -> None:
        poc: dict = {
            "transactions": {
                "traveler": {
                    "name": "test-name",
                    "group": "test-group General Traveler",
                    "email": 'testEmailTarget@slalom.com'
                },
                "line_of_business": "Airplane",
                "point_of_sale": "USA"
            }
        }
        try:
            request = sendEvent(poc)
            print(request, '---------- REQUEST ----------')
        except:
            raise Exception('Error')

    def process_record(self, record: dict, context: dict) -> None:
        """Process the record.

        Developers may optionally read or write additional markers within the
        passed `context` dict from the current batch.

        Args:
            record: Individual record in the stream.
            context: Stream partition or context dictionary.
        """
        # Sample:
        # ------
        # with open(context["file_path"], "a") as csvfile:
        #     csvfile.write(record)

    def process_batch(self, context: dict) -> None:
        """Write out any prepped records and return once fully written.

        Args:
            context: Stream partition or context dictionary.
        """
        # Sample:
        # ------
        # client.upload(context["file_path"])  # Upload file
        # Path(context["file_path"]).unlink()  # Delete local copy
