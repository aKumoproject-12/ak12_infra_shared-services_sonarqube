import requests, os                                 

url =   "https://heyimiana.com"                       
slack = "https://hooks.slack.com/services/B00000000/A00000000/XXXXXXXXXXXXXXXXXXXXXXXX"                     
headers = {"Content-type": "application/json"}
slack_id = A4569BGV97

 # This function allows to send a message to Slack with different data
def slack_sms(data):
    requests.post(url=slack, headers=headers, data=data)

# Try-except block for error handeling
try:
    response = requests.get(url)                    
    if response.status_code == 200:                 
        print(f"{url} is up!")
    else:
        print(f"Oops! Status code: {response.status_code}")

except requests.exceptions.ConnectionError:         
    slack_sms(data=f'{"text": ":rotating_light: Web Server: {url} is down :ahhhhhh: -- Set By {slack_id}"}')
except:
    print(f"{url} something went wrong!")
    slack_sms(data=f'{"text": "Web Server: {url} something went wrong -- Set By {slack_id}"}')