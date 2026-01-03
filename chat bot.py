import datetime
import time

name= input("Swagat hai, Enter your name :")
presentHour=datetime.datetime.now().hour

if 5<= presentHour<=11:
    print("Good morning,",name)
elif 11<=presentHour<=17:
    print("Good afternoon,",name)    
elif 17<=presentHour<=23:
    print("Good evening,",name)    
else:
    print("Good night,",name)

print("Namaste! Welcome to chat Bot" )
print("You can ask me basic question,type 'bye' to exit")

responses = {
    "hello":"Hii, welcome. how can i help you?",
    "how are you":"I'm fine.Thank you",
    "who are you":"I'm a smart AI chat bot based on python",
    "motivate me":"if u r going through hell keep going",
    "happy":"Great to hear that",
}
def getResponseofBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am not able to tell right now because i'm still in learning phase"
while True:
    userInput= input("Please ask your Question:")
    reply= getResponseofBot(userInput)    
    print("Bot Response :",reply)
    if "bye" in userInput.lower():
        break
