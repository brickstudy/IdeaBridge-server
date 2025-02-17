import os
import yaml

from src.common import src_path


CONFIG_YML_PATH = os.path.join(src_path, "config.yml")


def load_yml(file_path: str):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


_config = load_yml(CONFIG_YML_PATH)


class Config:
    def get_supabase():
        return _config["supabase"]

    def get_jwt():
        return _config["jwt"]
