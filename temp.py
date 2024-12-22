import requests
linkedin_profile_url = "https://www.linkedin.com/in/akshat-phadtare-7a3235218"

api_key = 'Mo9x2yez3uHbqb_fpcrWJw'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'#company/job/count'
params = {
    'url': linkedin_profile_url
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())