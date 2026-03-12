import requests

### CVE API endpoint 
### get all CVEs from NVD
response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0")

## Check if the request was successful 
if response.status_code == 200:
    cve_data=response.json()
    for cve in cve_data['vulnerabilities']:
       print(cve)
else:
    print(f"Failed to retrieve CVE data. Status code: {response.status_code}")

