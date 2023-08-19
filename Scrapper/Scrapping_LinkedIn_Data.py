import requests
import json
import cgi,cgitb

PROXYCURL_API_KEY = 'd126ff0f-6421-47ab-9ed6-8ec55d843442'

def get_profile(profile_id):
    data = cgi.FieldStorage
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': f'https://www.linkedin.com/in/{profile_id}/',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    
    output =  (response.json())
    
    
    
    #with open("Scrap_data.json", "w") as outfile:
     #   json.dump(output, outfile)

    return output    

    
get_profile("harshil-9039ba207")