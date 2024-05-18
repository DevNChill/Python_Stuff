import pyttsx3
engine = pyttsx3.init()
x = input("type what you want to speak : \n")
engine.say(x)
engine.runAndWait()
engine.stop()