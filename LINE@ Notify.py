import requests, schedule, time

def sendtoNotify():
    token = "oWREJ7eRWI7CQscwvPalLZrcu4klQ5R0MXFJwSDCdm5"
    content = "Take a bath, take a bed again"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {token}",
    }
    url = "https://notify-api.line.me/api/notify"
    message = f"\n{content}"
    r = requests.post(url=url, headers=headers, data={"message": message})


schedule.every().day.at("06:00").do(sendtoNotify)

while True:
    schedule.run_pending()
    time.sleep(1)