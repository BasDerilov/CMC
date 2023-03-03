import json
import os


def set_vars_from_json(file: str):
    with open(file) as env_file:
        data = json.load(env_file)

        for var in data:
            print(f"setting {var}={data[var]}")
            os.environ.setdefault(var, data[var])

    return 0


def require_var(var_name: str) -> str:
    env_var = os.environ.get(var_name)

    if env_var is None:
        print(f"Enter a value for: {var_name}")

        raise Exception(f"Missing environment variable ${var_name}")

    return env_var