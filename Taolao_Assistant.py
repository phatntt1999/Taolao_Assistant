import speech_recognition
import pyttsx3

robot_listening = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_listening.listen(mic)
try:
    user = robot_listening.recognize_google(audio)
except:
    user = ""

print("You: " + user)
#================Listen=================#
if (user == ""):
    robot_brain = ""
    print("Robot: I can't hear you!")
elif (user == "Hello" or user == "hello"):
    robot_brain = "Hello"
    print("Robot: Hello, What you name?")
else:
    robot_brain = "Thank you!"
    print("Robot: Thank you!")

#==============Handle==================#
robot_say = pyttsx3.init()
rate = robot_say.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
robot_say.setProperty('rate', 150)     # setting up new voice rate

robot_say.say(robot_brain)
robot_say.runAndWait()

#==============Speak==================#