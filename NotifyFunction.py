import urllib.parse
import requests, sys

__author__ = "> Alif Budiman"
__idline__ = "\n> ID Line: alifbudimanwahabbi"
__status__ = "\n> Send bug if you find it!!!"

"""
CREDIT ________________________________
⌬   Creat with ❤️ by Alip
⌬   find me on LINE or IG
⌬   ID: alifbudimanwahabbi 
⌬   ID LINE: alifbudimanwahabbi
⌬   Whatsapp +6282113791904
⌬   You can DM me for any ask something or give a littlebit donations
⌬   Copyright 2021 by Alip  FXG TEAMS
# Free to use, all credits belong to me.
# Feel free to report bugs :)"""


class LINE_Notify:
    """
    data 1 must be filled, other data is optional, default set as empty String
    """

    def __init__(self, access1, access2="", access3=""):
        self.NotifyHost = "https://notify-api.line.me/api/"
        self.Host = f"{self.NotifyHost}notify"
        self.HotsForStatus = f"{self.NotifyHost}status"
        self.HotsForRevoke = f"{self.NotifyHost}revoke"
        self.token1 = access1
        self.token2 = access2
        self.token3 = access3
        scoop_me_ice_cram = [__author__, __idline__, __status__]
        if scoop_me_ice_cram != []:
            for wanna_ice_cream in scoop_me_ice_cram:
                print(wanna_ice_cream)
        else:
            print("i'm mad with u :(")

    def MultiAccess(self, access):
        """
        for make sure and overcome your error in input token
        """
        if access == 1:
            return self.token1
        elif access == 2:
            if self.token2 != "":
                return self.token2
            else:
                print("Access Token 2 is empty, switch to Access Token 1")
                return self.token1
        elif access == 3:
            if self.token3 != "":
                return self.token3
            else:
                print("Access Token 2 is empty, switch to Access Token 1")
                return self.token1

    def sendMessage(self, content, access=1):
        """
        Notify send Message
        the data of content must String
        and access must Integer (you can change the number to change the access token)

        Examp
        content: "Hello world"
        access: 1 / 2 / 3 (oprional, defaulut set = 1)
        """
        Ntoken = self.MultiAccess(access)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {Ntoken}",
        }
        message = f"\n{content}"
        r = requests.post(self.Host, headers=headers, data={"message": message})
        print(r.text)

    def sendImage(self, file, content="\n", access=1):
        """
        Notify upload & send Image
        the data of file must your file phat (in string)
        and access must Integer (you can change the number to change the access token).
        content must String (optional, default set as "↵ " enter)

        Examp
        file: "tmpIMG/FXG (1).png"
        content: "Hello world"
        access: 1 / 2 / 3 (oprional, defaulut set = 1)
        """
        Ntoken = self.MultiAccess(access)
        file = {"imageFile": open(file, "rb")}
        data = {"message": content}
        headers = {"Authorization": f"Bearer {Ntoken}"}
        session = requests.Session()
        r = session.post(self.Host, headers=headers, files=file, data=data)
        print(r.text)

    def sendSticker(self, stkpkgid, stkid, content="\n", access=1):
        """
        Notify send Sticker
        the data of stkpkgid must sticker package ID (in Integer)
        and stkid must sticker ID (in Integer).
        you can check in #List of available stickers
        https://developers.line.biz/en/docs/messaging-api/sticker-list/

        access must Integer (you can change the number to change the access token)
        and content must String (optional, default set as "↵ " enter)

        Examp
        stkpkgid: 1
        stkid: 41
        content: "Hello world"
        access: 1 / 2 / 3 (oprional, defaulut set = 1)
        """
        Ntoken = self.MultiAccess(access)
        data = {"message": content, "stickerPackageId": stkpkgid, "stickerId": stkid}
        headers = {"Authorization": f"Bearer {Ntoken}"}
        session = requests.Session()
        r = session.post(self.Host, headers=headers, data=data)
        print(r.text)

    def cekApiStatus(self, notifytoken, access=1):
        """
        cek status api notify
        """
        Ntoken = self.MultiAccess(access)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {Ntoken}",
        }
        statusapi = requests.get(
            self.HotsForStatus,
            headers={"Authorization": f"Bearer {notifytoken}"},
        )
        messagestat = "Other: Processed over time or stopped"
        if statusapi.status_code == 200:
            messagestat = "200: Success・Access token valid"
        elif statusapi.status_code == 401:
            messagestat = "401: Invalid access token"
        else:
            pass
        r = requests.post(self.Host, headers=headers, data={"message": messagestat})
        print(r.text)
    
    
    def revokeToken(self, notifytoken, access=1):
        """
        for Revoke notify token
        """
        if notifytoken == self.token1:
            print("You can't revoke your token used on this script")
        elif self.token2 != "":
            if notifytoken == self.token2:
                print("You can't revoke your token used on this script")
        elif self.token3 != "":
            if notifytoken == self.token2:
                print("You can't revoke your token used on this script")
        else:
            Ntoken = self.MultiAccess(access)
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Bearer {Ntoken}",
            }
            statusapi = requests.post(
                self.HotsForRevoke,
                headers={"Authorization": f"Bearer {notifytoken}"},
            )
            messagestat = "404: Unknow Error"
            if statusapi.status_code == 200:
                messagestat = f"200: Success Revoke {notifytoken}"
            elif statusapi.status_code == 401:
                messagestat = f"401: Invalid access token {notifytoken}"
            else:
                pass
            r = requests.post(self.Host, headers=headers, data={"message": messagestat})
            print(r.text)
    
    
