import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if response.status_code == 200:
    pull_requests = response.json()
    #print(output[0])
    output = {}
    for item in pull_requests:
        creator = item["user"]["login"]
        if creator in output:
            output[creator]+=1
        else:
            output[creator] = 1
        
    print(output)
else:
    print(f"Fail to fetch dataw with status code:{response.status_code}")