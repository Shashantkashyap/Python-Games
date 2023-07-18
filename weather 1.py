import requests
import json
import pyttsx3
import time
while True:
    x = input("enter city name")
    url = f"http://api.weatherapi.com/v1/current.json?key=3b617a4764d147f09db115019230807&q={x}"
    r = requests.get(url)
    # print(r.text)
    z = json.loads(r.text)
    text = pyttsx3.init()
    text.say("the temprature is")
    time.sleep(1)
    text.say(z["current"]["temp_c"])
    text.runAndWait()
    text.say("degree celcius")
    text.runAndWait()
    time.sleep(2)
    print(z["current"]["temp_c"])
