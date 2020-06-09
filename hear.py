import speech_recognition

robot_listening = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_listening.listen(mic)
try:
    user = robot_listening.recognize_google(audio)
except:
    user = ""

print("You: " + user)


