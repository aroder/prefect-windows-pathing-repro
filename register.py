from importlib import import_module

import prefect
from prefect.environments.storage import Docker
from prefect.client.client import Client
from prefect.environments import LocalEnvironment

flow = import_module('flow').flow
flow.storage = Docker(
    registry_url='adamroderick/prefect-windows-pathing-repro',
    python_dependencies=['boto3'],
    dockerfile='Dockerfile'
)
flow.environment = LocalEnvironment()

flow.register(
    project_name='dtdev',
    labels=['dev', 'do_not_run']
)