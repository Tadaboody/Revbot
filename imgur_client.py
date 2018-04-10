import requests
from collections import namedtuple
class Imgur:
    BASE_URI = "https://api.imgur.com/3/"
    
    @staticmethod
    def endpoint(*nodes):
        return Imgur.BASE_URI + '/'.join(nodes)

    def __init__(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {'Authorization':'Client-ID {client_id}'.format(client_id=self.client_id)}
    
    def delete_image(self,image):
        request = requests.delete(self.endpoint('image',image['imageDeleteHash']))
        request.raise_for_status()
        return request.json['success']

    def upload_image(self, path):
        url = self.endpoint('image')
        files = {'image':open(path)}
        request = requests.post(url=url,files=files,headers=self.headers)
        request.raise_for_status()
        return request.json