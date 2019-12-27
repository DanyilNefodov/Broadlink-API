import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Index: {index}\nName: {name}\n")