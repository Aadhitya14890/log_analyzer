# config.py

import logging
import json

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)



def setup_logging(config):
    logging.basicConfig(
        filename=config["log_file"],
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )