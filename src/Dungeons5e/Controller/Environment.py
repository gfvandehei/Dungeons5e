from typing import List
from os import PathLike
import os
from dotenv import dotenv_values, find_dotenv

class Dungeons5eEnvironmentHandler(object):

    def __init__(self, env_file_paths: List[PathLike]):
        self._env = {}
        for env_path in env_file_paths:
            config = dotenv_values(str(env_path))
            self._env.update(config)
    
    def get_env(self, key, default=None):
        loaded_env_files_value = self._env.get(key, default)
        if loaded_env_files_value == default:
            value = os.getenv(key)
            if value is None:
                return default
            else:
                return value
        return loaded_env_files_value

    def get_env_bool(self, key, default=None):
        value = self.get_env(key, None)
        if value is None:
            return default
        else:
            if value.lower() in ["false", "f"]:
                return False
            else:
                return True
    