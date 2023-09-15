import requests

url = "https://hbone.hepsiburada.com:2001/awcm/statistics"

payload = {}
headers = {}

response = requests.request("LINK", url, headers=headers, data=payload)

if (response.status_code!=200):
    print("servis ayakta")
    
else:
    print("servis down")



