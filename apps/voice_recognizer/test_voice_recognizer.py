import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Say something")
    audio = r.listen(source)

# r.recognize_bing(audio, language="ru-Ru"))
query = r.recognize_sphinx(audio)
print(f"You said: {query}")
