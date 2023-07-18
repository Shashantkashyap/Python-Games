import pyttsx3 as p
text=p.init()
while True:
    x = input("say ")
    if x=="quit":
        text.say("bye bye ")
        text.runAndWait()
        break

    text.say(x)
    text.runAndWait()

