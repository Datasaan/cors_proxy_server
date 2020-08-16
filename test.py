
import requests
url = 'http://localhost:9236/doc_app'
data = {'inputs':['My son is vomiting.']}
requests.post(url,json = data)
