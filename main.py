import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/AU/AUD/en-US/MEL-sky/SYD-sky/2020-11-03"

querystring = {"inboundpartialdate":"2020-12-05"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "fa98bed2d4mshbf19405106ccc0bp14c91djsn9fe248ea1d29"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
