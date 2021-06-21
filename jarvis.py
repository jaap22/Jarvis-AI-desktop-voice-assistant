import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
from ecapture import ecapture as ec
import wolframalpha


engine = pyttsx3.init('sapi5')#sapi5 is used to take the voice
voices=engine.getProperty('voices')
# print(voices[0].id) 
# only check which voices are available in computer
engine.setProperty('voice',voices[0].id) 
# use 0 for boy and 1 for girl


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak(" I am jarvis sir pls tell me how may I help you")   

def takecommand():
# Initialize the recognizer
    r=sr.Recognizer()
    #  use the microphone as source for input.
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
         #listens for the user's input 
        audio=r.listen(source)
    
    try:
        # Using ggogle to recognize audio 
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        
        print("say that again pls")
        return "None"
    return query
  
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('1803162.cse.cec@cgc.edu.in','8872842121')
    server.sendmail('1803162.cse.cec@cgc.edu.in',to,content)
    server.close()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week) 
  



if __name__ == '__main__':

        
         wishMe()
         while True:
             query=takecommand().lower()#logic for exequting tasks based on query
             if 'wikipedia' in query:
                 speak("searhing wikipedia")
                 query=query.replace("wikipedia","")
                 results=wikipedia.summary(query,sentences=2)
                 speak("According to wikipedia")
                
                 speak(results)
                 print(results.encode("utf-8"))

             elif 'open youtube' in query:
                 webbrowser.open("www.youtube.com")

             elif 'open google' in query:
                 webbrowser.open("www.google.com")

             elif 'stackoverflow' in query:
                 webbrowser.open("www.stackoverflow.com")
              
             elif 'play music' in query :
                 speak("Here you go with music")
                 music_dir = "E:\\songs"
                 songs = os.listdir(music_dir)
                 print(songs)    
                 random = os.startfile(os.path.join(music_dir, songs[0]))
            
             elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Mam, the time is {strTime}")

             
             elif 'open eclipse' in query:
                 codePath = r"C:\\Users\\CW\\eclipse\\java-2019-06\\eclipse\\eclipse.exe"
                 os.startfile(codePath)
             
             elif 'email to harry' in query:
                 try:
                     speak("What should I say?")
                     content = takecommand()
                     to = "jaapkaur092000@gmail.com"   
                     sendEmail(to, content)
                     speak("Email has been sent !")
                 except Exception as e:
                     print(e)
                     speak("I am not able to send this email")
                      
             elif 'open geeks for geeks' in query:
                 speak("Opening GeeksforGeeks ")
                 webbrowser.open("www.geeksforgeeks.com") 
            
             elif "who are you" in query: 
                 speak("I am Jarvis. Your deskstop Assistant")

             elif "which day it is" in query:
                 tellDay() 

             elif 'how are you' in query:

                 speak("I am fine, Thank you")
                 speak("How are you, mam")

             
             elif 'fine' in query or "good" in query:


                 speak("It's good to know that your fine")

             
             elif "who made you" in query or "who created you" in query: 

                 speak("I have been created by jaap.")

             elif "who i am" in query:

                speak(" you speak so definitely you are a human")

             elif "why you came to world" in query:

                 speak("Thanks to jaap. but It's a secret")

             elif ' what is love' in query:


                 speak("It is 7th sense that destroy all other senses")

             elif 'reason for your creation' in query:
                 speak("I was created as a Major project by jaap")
                

             elif "will you be my gf" in query or "will you be my bf" in query: 
                 
                 speak("I'm not sure about, may be you should give me some time")

             elif "i love you" in query:
                 speak("It's hard to understand")

             elif 'joke' in query:
                 speak(pyjokes.get_joke())

             elif "camera" in query or "take a photo" in query:

                 ec.capture(0, "Jarvis Camera ", "img.jpg")


            