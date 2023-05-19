#!/usr/bin/env python3
import time
import requests
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def check_wifi(ip_address):
    try:
        response = requests.get(f"http://{ip_address}:5000/status", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def send_slack_message():
    slack_token = os.environ["SLACK_API_TOKEN"]
    client = WebClient(token=slack_token)
    try:
        response = client.chat_postMessage(
            channel='#general',
            text="The Wi-Fi connection to the monitored machine was lost but is now back online!")
    except SlackApiError as e:
        # You might want to log this error in real life
        print(f"Error: {e.response['error']}")

def main():
    ip_address = "192.168.1.2"  # replace with your machine's local IP address
    connection_lost = False
    while True:
        if not check_wifi(ip_address):
            connection_lost = True
        elif connection_lost:
            send_slack_message()
            connection_lost = False
        time.sleep(60)  # check every 60 seconds

if __name__ == '__main__':
    main()
