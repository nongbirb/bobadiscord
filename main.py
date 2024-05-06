from http.client import HTTPSConnection
from sys import stderr
from json import dumps, loads  # Include loads for parsing JSON response
from time import sleep
import json
import random

# Load Config
with open('./config.json') as f:
    data = json.load(f)
    c = data['Config'][0]
    print('Loading...')
token = c['token']
channelids = c['channelids']  # List of channel IDs
messages = c['messages']

header_data = {
    "content-type": "application/json",
    "user-agent": "discordapp.com",
    "authorization": token
}

def get_connection():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v9/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()
        response_body = resp.read()

        if 199 < resp.status < 300:
            print("Message Sent")
            # Parse the response to get the message ID
            message_id = json.loads(response_body)['id']
            # Immediately delete the message
            delete_message(conn, channel_id, message_id)
        else:
            stderr.write(f"HTTP {resp.status}: {resp.reason}\n")

    except Exception as e:
        stderr.write(f"Error: {str(e)}\n")

def delete_message(conn, channel_id, message_id):
    try:
        conn.request("DELETE", f"/api/v9/channels/{channel_id}/messages/{message_id}", headers=header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            print("Message Deleted")
        else:
            stderr.write(f"Failed to delete message, HTTP {resp.status}: {resp.reason}\n")
    except Exception as e:
        stderr.write(f"Error while deleting message: {str(e)}\n")

def main():
    random_channel_id = random.choice(channelids)  # Randomly select a channel ID
    message_data = {
        "content": random.choice(messages),  # Randomly select a message
        "tts": "false"
    }

    send_message(get_connection(), random_channel_id, dumps(message_data))

if __name__ == '__main__':
    while True:
        main()
        sleep(random.randint(62, 63))  # Randomize sleep time between 120 and 150 seconds
