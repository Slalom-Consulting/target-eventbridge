import os

AWS_SERVICE_NAME = "operations-travel"
Region = os.environ.get("AWS_REGION")
AWS_REGION = f'{Region}'

# Client config used by both Eventbridge.
AWS_CLIENT_CONFIG = { "region": AWS_REGION }

# Event Bus name used by the gapiMockData.request.ts file in order to route the payload to the expected location
AWS_BUS_NAME = "operationsEventBus"
Environment = os.environ.get("Environment")
AWS_EVENT_BUS_NAME = f"{Environment}_{AWS_BUS_NAME}"

# Payload Source
PAYLOAD_SOURCE_EMPLOYEE = "people.employee"
PAYLOAD_SOURCE_PAYROLL = "people.payroll-result-line"
PAYLOAD_SOURCE_OPERTATIONS_EGENCIA = "operations.egencia"

# Payload detailTypes
PAYLOAD_DETAILTYPE_EMPLOYEE_CHANGE = "employee.change"
PAYLOAD_DETAILTYPE_EMPLOYEE_HIRE = "employee.hire"
PAYLOAD_DETAILTYPE_EMPLOYEE_HIRE_RESCIND = "employee.hire-rescind"
PAYLOAD_DETAILTYPE_EMPLOYEE_TERMINATE = "employee.terminate"
PAYLOAD_DETAILTYPE_EMPLOYEE_TERMINATE_RESCIND = "employee.terminate-rescind"
PAYLOAD_DETAILTYPE_BULK_FILE = "bulkfile.create"
PAYLOAD_DETAILTYPE_OPERATIONS_EGENCIA_TRANSACTIONS="egencia.transactions"