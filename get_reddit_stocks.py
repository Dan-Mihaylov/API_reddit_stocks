import requests


class GetInfo:

    def __init__(self, path: str):
        self.path = path
        self.information = []

    def retrieve_info(self):
        response = requests.get(self.path)
        self.information = response.json()

    def get_info(self):
        return self.information

    def sort_ascending(self):
        sorted_information = sorted(self.information, key=lambda x: x["no_of_comments"])
        return sorted_information

    def sort_descending(self):
        sorted_information = sorted(self.information, key=lambda x: -x["no_of_comments"])
        return sorted_information

