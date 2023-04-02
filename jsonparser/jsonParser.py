#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Little Json file parsing module helper
"""
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JsonFile:
    """ Little Json file parsing module helper """
    def __init__(self, file: str):
        self.file = Path(file)
        if not self.file.name:
            raise ValueError('No file name provided')

    def load(self) -> dict:
        """ Load JSON file """
        try:
            with self.file.open('r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                return data
        except Exception as error:
            logger.error(f"Error loading JSON file {self.file}: {error}")
            raise

    def save(self, data: dict) -> None:
        """ Save JSON file """
        if not self.file.suffix.lower() == '.json':
            self.file = self.file.with_suffix('.json')

        try:
            with self.file.open('w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, sort_keys=False, indent=2,
                          separators=(',', ': '), ensure_ascii=False)
                logger.info(f"File saved: {self.file}")
        except Exception as error:
            logger.error(f"Error saving JSON file {self.file}: {error}")
            raise

if __name__ == '__main__':
    test_data_file = JsonFile("/tools/pipeline/structure/hdrFolderTemplate.json")
    test_data = test_data_file.load()
    print(test_data)
