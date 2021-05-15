import yaml

DELAY_TIMEOUT_KEY = "dialog_timeout"


def _read_yaml(filepath):
    with open(filepath, "r") as file:
        return yaml.load(file, yaml.FullLoader)


CONFIG = _read_yaml('resources/config.yaml')
