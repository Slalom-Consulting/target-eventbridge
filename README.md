# target-eventbridge

`target-eventbridge` is a Singer target for eventbridge.

Build with the [Meltano Target SDK](https://sdk.meltano.com).

### Configure using environment variables

This Singer target will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

## Configuration Specific to Target-Eventbridge

`event_bus_name` 
`event_detail_type` 
`event_source` 

These settings will need to be configured in order to run the target. 

Meltano will find these values from your `.env` first by looking for matching values taged with the prefix `TARGET_EVENTBRIDGE_`. ex. -> `TARGET_EVENTBRIDGE_EVENT_BUS_NAME`

the values from your .env can be overwritten by using the command `meltano config target-eventbridge set "variable_name" "variable_value"`


### Source Authentication and Authorization

AWS credentials are required for running target-eventbridge. To set your local `aws/credentials` run the following commands. 

`aws-azure-login --profile "your_profile_name"`

`aws configure`

# Note On Configuration

If multiple AWS_Profiles exist in your `.aws/credentials` file adding `AWS_PROFILE` to your `.env` file and pointing the value to the desired profile will allow you to target which profile will be used during runtime.

## Usage

You can easily run `target-eventbridge` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Target Directly

```bash
target-eventbridge --version
target-eventbridge --help
# Test using the "Carbon Intensity" sample:
tap-carbon-intensity | target-eventbridge --config /path/to/target-eventbridge-config.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `target-eventbridge` CLI interface directly using `poetry run`:

```bash
poetry run target-eventbridge --help
```

### Testing with [Meltano](https://meltano.com/)

_**Note:** This target will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd target-eventbridge
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke target-eventbridge --version
# OR run a test `elt` pipeline with the Carbon Intensity sample tap:
meltano elt tap-carbon-intensity target-eventbridge
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the Meltano Singer SDK to
develop your own Singer taps and targets.
