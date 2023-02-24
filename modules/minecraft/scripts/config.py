import yaml
import json
from pathlib import Path

import utils.logging as log


class Config:
    def write_properties(self, src_json: Path, tgt_properties: Path):
        log.started(f"converting {src_json} to {tgt_properties}")

        with open(tgt_properties, "w+") as file:
            data: dict = Config.get_data(src_json)

            for prop in data:
                print(f"{prop}={data[prop]}")

                file.write(f"{prop}={data[prop]}\n")

        log.success(f"coverted file {tgt_properties} with success")

    def write_yml(src_json: Path, tgt_yml: Path):
        log.started(f"converting {src_json} to {tgt_yml}")

        with open(tgt_yml, "w+") as file:
            data: dict = Config.get_data(src_json)
            yaml.dump(data, file)

        log.success(f"coverted file {tgt_yml} with success")

    def get_data(src: Path) -> dict:
        with open(src, "r") as file:
            return json.load(file)
