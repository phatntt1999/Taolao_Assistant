import pyttsx3

robot_brain = "Virtual Environment"

robot_say = pyttsx3.init()
rate = robot_say.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
robot_say.setProperty('rate', 150)     # setting up new voice rate


robot_say.say(robot_brain)
robot_say.runAndWait()
