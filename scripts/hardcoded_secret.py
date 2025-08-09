import requests, os                                 

url =   "https://lalalala.com"                       
slack = "https://hooks.slack.com/services/B15007023/A19780503/XXXXXXXXXXXXXXXXXXXXXXXX"                     
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


def check_value(value):
    if value < 0:
        raise BaseException("Value cannot be negative")
        #The BaseException class is reserved for system-level exceptions