import json
import os
import logging
from src.engine.utilities.logger.dev_logger import DevLogger
from src.engine.utilities.config.config_settings import ALL_DATA_FILES


class Dataloader:
    def __init__(self):
        # init
        self.Log = DevLogger(Dataloader).log
        self.cwd = os.getcwd()
        self.load_files = ALL_DATA_FILES
        self.Log(logging.INFO, 'init complete')

    def load_all_data(self):
        static_data = {}
        self.Log(logging.INFO, 'loading data...')
        for file_path in self.load_files:
            self.Log(logging.INFO, f'loading \'{file_path}\'...')
            try:
                file_string = f'{self.cwd}/{file_path}'
                with open(file_string, 'r') as file:
                    data = json.load(file)
            except Exception as error_code:
                self.Log(logging.ERROR, f'error loading \'{file_path}\': {error_code}')
            else:
                self.Log(logging.INFO, f'successfully loaded \'{file_path}\'')
                data_dict_key = str(self.load_files[file_path])
                static_data[data_dict_key] = data
        return static_data
