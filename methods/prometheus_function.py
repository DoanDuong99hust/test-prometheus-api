import json
from types import SimpleNamespace


class PrometheusFunctions():
    """docstring for PrometheusFunctions"""

    def __init__(self):
        pass

    @staticmethod
    def seperate_json_data(data):
        dict_data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        list_data = dict_data.data.result
        for data in list_data:
            data.value[1] = float(data.value[1])
        for data in list_data:
            return data.value
