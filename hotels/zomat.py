import os
import logging
import requests


class Zomat(object):
    """
    Fetch data using the Zomato API
    """

    def __init__(self):
        self.logger = logging.getLogger("Zomat")
        self.logger = ("Initialzing Zomat class")
        self.userKey = os.environ.get("USER-KEY")


    def getLocation(self, location):
        """
        Get Zomato entity_id and entity_type
        """
         headers={"Accept":"applicaiton/json", "user-key": self.userKey}
         search_url = "https://developers.zomato.com/api/v2.1/locations?query="+location
         search_resp=requests.get(search_url,headers=headers)
         search_resp_dict=json.loads(search_resp.text)
         loc_sug_list = search_resp_dict['location_suggestions']
         for loc_sug in loc_sug_list:
             entity_type = loc_sug["entity_type"]
             print (entity_type)
             entity_id = loc_sug["entity_id"]
             print (entity_id)
             return entity_id, entity_type