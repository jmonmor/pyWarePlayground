import requests

class APIClient:
  def __init__(self):
    pass
  
  def get_remote_file(self, url) -> dict:
    res = requests.get(url)
    return res.json()
     