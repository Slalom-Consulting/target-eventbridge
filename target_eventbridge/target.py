"""eventbridge target class."""

from __future__ import annotations

from singer_sdk.target_base import Target

from singer_sdk import typing as th

from target_eventbridge.sinks import (
    eventbridgeSink,
)

class Targeteventbridge(Target):
    
    name = "target-eventbridge"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "event_bus_name",
            th.StringType,
            description="The event_bus name to send the event to."
        ),
        th.Property(
            "event_detail_type",
            th.StringType,
            description="The detail type to use for the event. This determines which fields are included in the event."
        ),
        th.Property(
            "event_source",
            th.StringType,
            description="The event source to use for the event."
        ),
    ).to_dict()

    default_sink_class = eventbridgeSink


if __name__ == "__main__":
    Targeteventbridge.cli()
