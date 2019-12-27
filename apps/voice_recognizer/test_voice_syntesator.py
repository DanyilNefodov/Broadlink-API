import pyttsx3

engine = pyttsx3.init('sapi5')

engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0") 
engine.say("Privet")
engine.runAndWait()
