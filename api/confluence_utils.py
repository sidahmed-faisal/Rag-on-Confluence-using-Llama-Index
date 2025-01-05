from llama_index.readers.confluence import ConfluenceReader
import requests
from requests.auth import HTTPBasicAuth
import json



class Confluence_control:

    def __init__(self, url , user , password):
        self.url = url
        self.user = user
        self.password = password

    def get_documents_reader(self):

        try:
            reader = ConfluenceReader(base_url=self.url, user_name=self.user, password=self.password)

            return reader


        except Exception as e:
            return f"This Error has occured while trying to connect to the domain {self.url} : {e}"

    def load_documents(self, space):

        try:
            reader = self.get_documents_reader()

            documents = reader.load_data(
            space_key=space, include_attachments=True,page_status="current")

            return documents
        
        except Exception as e:
            return f"Error while trying to load documents from Space with key {space} : {e}"
        
    def load_pages(self, space):

        try:
            reader = self.get_documents_reader()
            documents = reader.load_data(
                space_key=space, include_attachments=True, page_status="current"
            )
            
            pages = {}
            for d in documents:
                pages[d.metadata["title"]] = d.metadata["page_id"]

                
            return pages
        except Exception as e:
            return f"Error while trying to load pages from Space with key {space} : {e}"
        
    def show_spaces(self):

        url = self.url

        spaces_url = url +"/api/v2/spaces"

        auth = HTTPBasicAuth(self.user, self.password)

        headers = {
        "Accept": "application/json"
        }

        response = requests.request(
        "GET",
        spaces_url,
        headers=headers,
        auth=auth
        )

        data = response.json()

        # Create a dictionary with the space name and key
        spaces_dict = {space['name']: space['key'] for space in data['results']}

        return spaces_dict        

        


        

# from llama_index.core.node_parser import SentenceSplitter

# parser = SentenceSplitter()

# nodes = parser.get_nodes_from_documents(documents)

# print(nodes)