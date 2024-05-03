import requests

chat_id = "6258976989"
urlp = "https://t.me/nhdbdd"
url = f"https://api.telegram.org/bot6314778606:AAFyvzVylI8Pvij_oLlGy1IXhZkso4r6DHY/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
