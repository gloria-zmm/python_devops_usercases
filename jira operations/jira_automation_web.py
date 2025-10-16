from flask import Flask,request
import requests
from requests.auth import HTTPBasicAuth
import json
import os
app = Flask(__name__)

@app.route('/createJira',methods = 'POST')
def createJira():


    url = "https://ximeizhu.atlassian.net/rest/api/3/issue"

    username = os.getenv("user_name")
    apitoken = os.getenv("apitoken")

    auth = HTTPBasicAuth(username, apitoken)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload_received = request.get_json()

    payload = json.dumps( {
    "fields": {



        "issuetype": {
        "id": "10007"
        },
        "project": {
        "id": "10001"
        },
        "summary": "this is the jira ticket",

    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)