# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
import argparse

def get_projects_name():

    url = "https://ximeizhu.atlassian.net/rest/api/3/project"

    username = os.getenv("user_name")
    apitoken = os.getenv("apitoken")

    auth = HTTPBasicAuth(username, apitoken)

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )

    output = json.loads(response.text)

    print([outputname["name"] for outputname in output])
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def get_issuetype_id(projectIdOrKey):
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
    import requests
    from requests.auth import HTTPBasicAuth
    import json

    url = f"https://ximeizhu.atlassian.net/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes"
    print(url)

    username = os.getenv("user_name")
    apitoken = os.getenv("apitoken")

    auth = HTTPBasicAuth(username, apitoken)

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def create_issues():
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org
    import requests
    from requests.auth import HTTPBasicAuth
    import json

    url = "https://ximeizhu.atlassian.net/rest/api/3/issue"

    username = os.getenv("user_name")
    apitoken = os.getenv("apitoken")

    auth = HTTPBasicAuth(username, apitoken)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {



        "issuetype": {
        "id": "10007"
        },
        "project": {
        "id": "10001"
        },
        "summary": "this is my first jira ticket",

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

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='My Script')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # get_issuetype_id
    hello_parser = subparsers.add_parser('get_issuetype_id', help='get_issuetype_id')
    hello_parser.add_argument('projectIdOrKey', help='rojectIdOrKey')

    # greet 命令
    greet_parser = subparsers.add_parser('create_issues', help='create_issues')

    args = parser.parse_args()

    if args.command == 'get_issuetype_id':
        get_issuetype_id(args.projectIdOrKey)
    elif args.command == 'create_issues':
        create_issues()
    else:
        parser.print_help()

        