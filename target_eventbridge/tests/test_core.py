import pytest

import target_eventbridge.helpers

from target_eventbridge.helpers.aws.ebHelper import (
    sendEvent
)

def test():
    testObject = {}
    with pytest.raises(Exception):
       sendEvent(testObject)
        