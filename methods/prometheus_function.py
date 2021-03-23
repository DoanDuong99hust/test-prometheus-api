import requests
import json
from types import SimpleNamespace
import time


class PrometheusFunctions():
    """docstring for PrometheusFunctions"""

    def __init__(self):
        pass

    def seperate_json_data(self, data):
        dict_data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        list_data = dict_data.data.result
        for data in list_data:
            return data.value
        

