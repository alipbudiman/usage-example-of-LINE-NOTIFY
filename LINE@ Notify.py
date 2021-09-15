import requests, schedule, time, json, requests

global token

"""
simpel using line notify methode
"""

token = "oWREJ7eRWI7CQscwvPalLZrcu4klQ5R0MXFJwSDCdm5"  # <  imput your notify token


def sendtoNotify(token, content="good morning bby..."):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {token}",
    }
    url = "https://notify-api.line.me/api/notify"
    message = f"\n{content}"
    r = requests.post(url=url, headers=headers, data={"message": message})
    print(r.text)


def prayer_schedule_updates(
    www_waktusholat_org="https://api.pray.zone/v2/times/today.json?city=",
    city="jakarta",
):
    data = json.loads(requests.get(www_waktusholat_org + city).text)
    if data["code"] == 200:
        goshalat = data["results"]["datetime"][0]["times"]
        datashalat["Fajr"] = goshalat["Fajr"]
        datashalat["Dhuhr"] = goshalat["Dhuhr"]
        datashalat["Asr"] = goshalat["Asr"]
        datashalat["Maghrib"] = goshalat["Maghrib"]
        datashalat["Isha"] = goshalat["Isha"]
    else:
        print("oops something wen worng...")


azan_woi = """
ADZAN WOI ADZAN!! SOLAT JANGAN MAIN LINE TERUS LO!!!
MANG LINE BAKAL JAMIN LO MASUK SORGA

(٢x) اَللهُ اَكْبَرُ،اَللهُ اَكْبَرُ
(٢x) أَشْهَدُ اَنْ لاَ إِلٰهَ إِلَّااللهُ
(٢x) اَشْهَدُ اَنَّ مُحَمَّدًا رَسُوْلُ اللهِ
(٢x) حَيَّ عَلَى الصَّلاَةِ
(٢x) حَيَّ عَلَى الْفَلاَحِ
(١x) اَللهُ اَكْبَرُ ،اَللهُ اَكْبَرُ
(١x) لَا إِلَهَ إِلَّااللهُ

"""
datashalat = {
    "city": "jakarta",
    "Fajr": "04:30",
    "Dhuhr": "11:48",
    "Asr": "15:02",
    "Maghrib": "18:03",
    "Isha": "18:55",
}
prayer_schedule_updates()
print("update prayer schedule")
for x in list(datashalat):
    print(str(x + ": " + datashalat[x]))

""""
Morning Greatings...
"""
schedule.every().day.at("06:00").do(sendtoNotify)

"""
Adzan
"""


def Fajr():
    sendtoNotify(token, content=azan_woi + "\n\nAdzan Fajr")


def Dhuhr():
    sendtoNotify(token, content=azan_woi + "\n\nAdzan Dhuhr")


def Asr():
    sendtoNotify(token, content=azan_woi + "\n\nAdzan Asr")


def Maghrib():
    sendtoNotify(token, content=azan_woi + "\n\nAdzan Maghrib")


def Isha():
    sendtoNotify(token, content=azan_woi + "\n\nAdzan Isha")


"""
schedule and waiting for Adzan
"""

schedule.every().day.at(datashalat["Fajr"]).do(Fajr)
schedule.every().day.at(datashalat["Dhuhr"]).do(Dhuhr)
schedule.every().day.at(datashalat["Asr"]).do(Asr)
schedule.every().day.at(datashalat["Maghrib"]).do(Maghrib)
schedule.every().day.at(datashalat["Isha"]).do(Isha)

"""
update prayer schedule
"""

schedule.every().day.at("23:40").do(prayer_schedule_updates)

while True:
    schedule.run_pending()
    time.sleep(1)
