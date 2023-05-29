import requests


class GetInfo:

    def __init__(self, path: str):
        self.path = path
        self.information = []
        self.response = requests.get(self.path)

    def retrieve_info_as_json(self):
        self.information = self.response.json()

    def info_as_text(self):
        return self.response.text

    def get_status_code(self):
        return self.response.status_code

    def get_info(self):
        return self.information

    def sort_ascending(self):
        sorted_information = sorted(self.information, key=lambda x: x["no_of_comments"])
        return sorted_information

    def sort_descending(self):
        sorted_information = sorted(self.information, key=lambda x: -x["no_of_comments"])
        return sorted_information

