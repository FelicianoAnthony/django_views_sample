import requests
from bs4 import BeautifulSoup
from . import CoinsFromXML
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()




class GetDataXml():
    
    def http_get(self):

        url = 'https://rest.coinapi.io/v1/exchanges/?output_format=xml'
        r = requests.get(url, verify=False)
        return r



    def parse_xml(self, response_xml, root_elem, sub_elem):
        """given a root xml element -- get a list of property under it"""
        soup = BeautifulSoup(response_xml.text, "lxml")

        list_item = []
        for i in soup.find_all(root_elem):
            for j in i.find_all(sub_elem):
                list_item.append(j.text)
        return sub_elem, list_item


    def create_dict_obj(self, return_list=False):

        res = self.http_get()

        exchange_tup = self.parse_xml(res, 'exchange', 'exchange_id')
        website_tup = self.parse_xml(res, 'exchange', 'website')
        name_tup = self.parse_xml(res, 'exchange', 'name')


        task_list = []
        count=1
        for h,i,j in zip(exchange_tup[1], website_tup[1], name_tup[1]):
            z = CoinsFromXML(count, j,i,h)
            # z.exchange_id = h
            # z.website = i
            # z.name = j
            # z._id = count
            task_list.append(z)
            count+=1

        if return_list:
            return task_list


        dictionary = {}
        for x in range(len(task_list)):
            dictionary[x+1] = task_list[x]

        return dictionary


