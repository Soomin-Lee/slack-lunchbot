import json
import requests
from pandas.io.json import json_normalize


POST_MESSAGE_URL = 'https://slack.com/api/chat.postMessage'

def pushSlackMessage(token, channelId, message):
    headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
            'channel': channelId, 
            'text': message
    }

    res = requests.get(POST_MESSAGE_URL, headers=headers, params=data)
    print(res.json())
