import requests
from datetime import datetime

pixe_url = "https://pixe.la/v1/users"
TOKEN = "abcdef123456"
USERNAME= "lathass"
GRAPH_ID = "graph1"

user_input = {
              "token":TOKEN,
              "username": USERNAME,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"

}

#response = requests.post(url=pixe_url, json=user_input)
 # print(response.text)

GRAPH_END_POINT = f"{pixe_url}/{USERNAME}/graphs"

graph_config = {
                "id":GRAPH_ID ,
                "name":"Cycling Graph",
                "unit":"Km",
                "type":"float",
                "color":"ajisai",

}

headers = {
               "X-USER-TOKEN":TOKEN

}
# response = requests.post(url=GRAPH_END_POINT, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()

POST_VALUE_URL = f"{pixe_url}/{USERNAME}/graphs/{GRAPH_ID}"
post_data = {
             "date":today.strftime("%Y%m%d"),
             "quantity":input("How many km did you cycle today?")

}
response = requests.post(url=POST_VALUE_URL, json=post_data, headers=headers)
print(response.text)